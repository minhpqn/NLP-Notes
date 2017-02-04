# Hướng dẫn cài đặt công cụ Opinion Extraction cho tiếng Nhật

Author: Phạm Quang Nhật Minh (FPT Technology Research Institute - FTRI)

## Giới thiệu

Bài viết hướng dẫn cách cài đặt công cụ [Opinion Extraction](https://alaginrc.nict.go.jp/opinion/index_e.html) cho tiếng Nhật.

Môi trường cài đặt:

- Mac OS X El Capitan 10.11.6

## Cài đặt CRF++

Link: [https://taku910.github.io/crfpp/](https://taku910.github.io/crfpp/)

Cài đặt CRF++ phiên bản 0.58

## Cài đặt iconv

```
brew install iconv
```

## Cài đặt gawk

```
brew install gawk
```

## Cài đặt JUMAN phiên bản 6.01


**Bước 1**:

```
configure --prefix=PATH
```

Trong đó PATH là đường dẫn tới thư mục mà bạn muốn cài đặt

**Bước 2**:

```
make
```

Lỗi khi gõ lệnh ./make trong cài đặt JUMAN 6.01 trên Mac OS X El Capitan 10.11.6

```
sed: RE error: illegal byte sequence
```

Cách giải quyết: thiết lập các biến môi trường sau đây:

```
export LC_CTYPE='C'
export LANG='C'
export LC_ALL='C'
```

Tham khảo: [http://stackoverflow.com/questions/19242275/re-error-illegal-byte-sequence-on-mac-os-x/19770395#19770395](http://stackoverflow.com/questions/19242275/re-error-illegal-byte-sequence-on-mac-os-x/19770395#19770395)


**Bước 3**:

```
make install
```

**Bước 4**: Thiết lập đường dẫn tới thư mục cài đặt

Thêm dòng sau vào file cấu hình ```~/.bashrc```

```
export PATH=/Users/minhpham/nlp/local-tools/juman-6.01/bin:$PATH
```

### Test cài đặt JUMAN

Sau khi cài hoàn thành việc cài đặt Juman 6.01, chúng ta sẽ thử sử dụng JUMAN 
để phân tích câu tiếng Nhật.

Chúng ta sẽ sử dụng file sample ```sample.txt``` trong cùng thư mục.

Một số chú ý khi sử dụng JUMAN 6.01

- JUMAN bản 6.01 nhận đầu vào có encoding là EUC-JP nên nếu encoding của file 
text đầu vào phải là UTF-8 thì chúng ta cần chuyển định dạng sang EUC-JP trước
khi chạy tool. Chúng ta có thể dùng tool ```iconv``` hoặc lv để thực hiện công 
việc chuyển đổi character encoding.
- Khi muốn hiển thị kết quả phân tích của JUMAN 6.01, chúng ta cần chuyển ngược
lại từ EUC-JP sang UTF-8

Cách sử dụng như sau:

```
cat sample.txt | iconv -f UTF-8 -t EUC-JP | juman | iconv -f EUC-JP -t UTF-8
```

## Cài đặt KNP phiên bản 3.01

Download KNP bản 3.01 tại: [http://nlp.ist.i.kyoto-u.ac.jp/EN/index.php?KNP](http://nlp.ist.i.kyoto-u.ac.jp/EN/index.php?KNP)

Trước tiên, bạn cần cài đặt các công cụ sau đây:

- JUMAN phiên bản 6.0 hoặc mới hơn ([http://nlp.kuee.kyoto-u.ac.jp/nl-resource/juman.html](http://nlp.kuee.kyoto-u.ac.jp/nl-resource/juman.html))
- Thư viện [TinyCDB](http://www.corpit.ru/mjt/tinycdb.html)

### Cài đặt thư viện TinyCDB

- Download mã nguồn TinyCDB
- Make sử dụng lệnh ```make```
- Install TinyCDB sử dụng ```sudo make install```.

### Cài đặt KNP

Các bước cài đặt KNP như sau:

**Bước 1**: Set các giá trị cần thiết như sau để tránh lỗi
```sed: RE error: illegal byte sequence```

```
export LC_CTYPE='C'
export LANG='C'
export LC_ALL='C'
```

**Bước 2**: Configure

```
./configure --prefix=/Users/minhpham/nlp/local-tools/knp-3.01 --with-juman-prefix=/Users/minhpham/nlp/local-tools/juman-6.01
```

Trong môi trường bạn cài đặt, chú ý cần thay thế các đường dẫn tương ứng cho phù hợp.

**Bước 3**:

```
make
```

**Bước 4**:

```
make install
```

**Bước 5**: Thiết lập đường dẫn

Thêm dòng sau vào file cấu hình ```~/.bashrc```

```
export PATH=/Users/minhpham/nlp/local-tools/knp-3.01/bin:$PATH
```

### Test cài đặt KNP 3.01

Chú ý input đầu vào của KNP 3.01 có character encoding là EUC-JP nên bạn cần 
dùng chương trình ```iconv``` hoặc ```lv``` để convert sang định dạng thích hợp.

Dùng lệnh sau trong thư mục hiện tại (chứa file ```sample.txt```) để kiểm tra xem
bạn đã cài đặt KNP phiên bản 3.01 thành công chưa.

```
cat sample.txt | iconv -f UTF-8 -t EUC-JP | juman -e2 -B | knp | iconv -f EUC-JP -t UTF-8
```

Nếu bạn ra kết quả tương tự như sau thì bạn đã hoàn tất việc cài đặt.

# S-ID:1 KNP:3.01-CF1.0 DATE:2017/02/04 SCORE:-37.91003
子どもは──┐　
リンゴが──┤　
        すきだ。
EOS

## Cài đặt Opinion Extraction tool

Sau khi cài đặt tất cả các thư viện, công cụ cần thiết, chúng ta sẽ cài đặt
Opinion Extraction tool theo các bước sau đây.

**Bước 1**: Download công cụ tại trang Web
[Opinion extraction tool](https://alaginrc.nict.go.jp/opinion/index_e.html)

**Bước 2**: Giải nén 

```
tar xvfz extractopinion-1.2.tar.gz 
```

**Bước 3**: 

```
% cd svmtools/
% make clean ; make
```

**Bước 4**:

```
% cd ../pol/
% make clean ; make
```

Chú ý khi cài đặt:

- Copy các file ```dictionary.dic``` và ```reverse.dic``` (đính kèm email) vào thư mục ```./dic```.
- Có thể phải sửa lại đường dẫn tới gawk trong các file *.awk tương ứng cho thích 
hợp. Ví dụ trong Mac OS X cần sửa lại thành: ```#!/usr/local/bin/gawk -f```.

## Tài liệu tham khảo

- [Opinion extraction tool](https://alaginrc.nict.go.jp/opinion/index_e.html)