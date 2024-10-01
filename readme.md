# GlobalProtectClientDownloader  

## 日本語

### 概要  

Palo Alto Networks(以降、パロアルトと表記します)が提供するVPNサービス"Global Protect"のクライアントインストーラーを入手するためのPython GUIプログラムです。  
接続先はパロアルトが配信用に提供するAWS S3ストレージを利用しています。  

### 仕組み

パロアルトのGlobal ProtectはAWS S3ストレージ上に公式のクライアントインストーラーがホスティングされています。  
PanoramaやPanOSと同じ(と思われる)エンドポイントを利用することにより、グローバルに公開されている不特定多数のGlobal Protectエンドポイントを駆けずり回ってインストーラーを探す必要はもうありません。  
このツールを使えば、ワンクリックで特定のバージョン、最新のバージョンのGlobal Protectクライアントインストーラーを入手することが出来ます。  
もちろん、このツールを使用せずに直接[S3ストレージ](https://pan-gp-client.s3.amazonaws.com)にアクセスしてダウンロードすることもできます。  
例えば`<Key>0.0.0-00/GlobalProtect.msi</Key>`が必要なら、次のURLを開くことでダウンロードすることが出来ます。  
`https://pan-gp-client.s3.amazonaws.com/0.0.0-00/GlobalProtect.msi`  

また、それぞれのファイル名は下記の違いがあります。  

| ファイル名 | OS | 補足 |
| ---- | ---- | ---- |
| GlobalProtect.msi | Windows | 32bit(x86)用 |
| GlobalProtect64.msi | Windows | 64bit(x64)用 |
| GlobalProtect.pkg | macOS |  |

### 使い方  

releaseから最新のexeをダウンロードして起動してください。  
GlobalProtectクライアントのインストーラがプルダウンから選択できます。  
ダウンロードを押して保存先を指定するとダウンロードが行われます。
言語を変更したい場合、ソースコード内の`lang=`をオーバーライドすることで表示言語を変更することが出来ます。  
現時点では日本語・英語・中国語・???に対応しています。  


### 注意事項

- 本ソフトウェアは個人によって開発されており、パロアルトを含むいかなる公式な団体や組織により承認または公認されているものではありません
- 本ソフトウェアの使用に関して発生するいかなる損害についても、開発者は一切の責任を負いません  
これには、直接的、間接的、偶発的、特別な損害、または結果的な損害が含まれますが、これに限られません
- 本ソフトウェアは「現状のまま」提供されており、特定の目的に対する適合性、正確性、完全性、または本ソフトウェアの使用に関して発生する問題に関する明示または黙示の保証は一切行いません  
ユーザーは自己責任で本ソフトウェアを使用するものとします

## English

### WARNING

This readme and the text in the code are machine translated.  
Therefore, they may not be appropriate. Please understand. Thank you.

### Overview

This is a Python GUI program to obtain the client installer for the VPN service "Global Protect" provided by Palo Alto Networks (hereinafter referred to as Palo Alto).

The connection destination uses AWS S3 storage provided by Palo Alto for distribution.

### How it works

Palo Alto's Global Protect hosts the official client installer on AWS S3 storage.

By using the same (presumably) endpoint as Panorama and PanOS, you no longer need to run around looking for an installer on the numerous Global Protect endpoints available globally.

With this tool, you can get the latest version of the Global Protect client installer for a specific version with one click.

Of course, you can also download it by directly accessing [S3 storage](https://pan-gp-client.s3.amazonaws.com) without using this tool.

For example, if you need `<Key>0.0.0-00/GlobalProtect.msi</Key>`, you can download it by opening the following URL.
`https://pan-gp-client.s3.amazonaws.com/0.0.0-00/GlobalProtect.msi`

Also, the file names differ as follows.

| File name | OS | Supplementary information |
| ---- | ---- | ---- |
| GlobalProtect.msi | Windows | For 32bit (x86) |
| GlobalProtect64.msi | Windows | For 64bit (x64) |
| GlobalProtect.pkg | macOS | |

### How to use

Download the latest exe from release and launch it.
You can select the GlobalProtect client installer from the pull-down menu.
Press Download and specify the save destination to download.
If you want to change the language, you can change the display language by overriding `lang=` in the source code.
Currently, it supports Japanese, English, Chinese, and ???.

### Notes

- This software has been developed by an individual and has not been approved or certified by any official group or organization, including Palo Alto.
- The developer assumes no responsibility for any damages arising from the use of this software.
This includes, but is not limited to, direct, indirect, incidental, special, or consequential damages.
- This software is provided "as is" and does not provide any express or implied warranty regarding suitability for a particular purpose, accuracy, completeness, or problems arising from the use of this software.
The user shall use this software at his/her own risk.

## 中文

### 警告

本自述文件以及代码中的文本均经过机器翻译。
因此，它可能不合适。注意。谢谢。

### 概述

这是一个Python GUI程序，用于获取Palo Alto Networks（以下简称Palo Alto）提供的VPN服务“Global Protect”的客户端安装程序。
连接目标使用 Palo Alto 提供的 AWS S3 存储进行分发。

### 结构

Palo Alto 的 Global Protect 有一个托管在 AWS S3 存储上的官方客户端安装程序。
通过使用与 Panorama 和 PanOS 相同（或看起来如此）的端点，不再需要通过未指定数量的全球发布的 Global Protect 端点来搜索安装程序。
使用此工具，您只需一键即可获取最新版本的 Global Protect 客户端安装程序。
当然，您也可以不使用此工具，直接访问[S3存储](https://pan-gp-client.s3.amazonaws.com)并下载。
例如，如果您需要`<Key>0.0.0-00/GlobalProtect.msi</Key>`，则可以通过打开以下网址进行下载。
`https://pan-gp-client.s3.amazonaws.com/0.0.0-00/GlobalProtect.msi`

另外，各文件名还存在以下差异。

| 文件名 | OS |注释 |
| ---- | ---- | ---- |
| GlobalProtect.msi | Windows | 对于 32bit（x86）|
| GlobalProtect64.msi | Windows | 对于 64bit（x64） |
| GlobalProtect.pkg | macOS | |

### 如何使用

从发行版下载最新的 exe 并启动它。
您可以从下拉列表中选择 GlobalProtect 客户端安装程序。
单击“下载”并指定要下载的保存目的地。
如果要更改语言，可以通过覆盖源代码中的“lang=”来更改显示语言。
目前支持日语、英语、中文、???。


### 注释

- 该软件由个人开发，未经任何官方团体或组织（包括 Palo Alto）的认可或认证。  
- 开发商对因使用本软件而可能发生的任何损害不承担任何责任。
这包括但不限于直接、间接、偶然、特殊或后果性损害。
- 本软件按“原样”提供，对于特定用途的适用性、准确性、完整性或使用本软件可能出现的问题不作任何明示或暗示的保证。
用户应自行承担使用本软件的风险。