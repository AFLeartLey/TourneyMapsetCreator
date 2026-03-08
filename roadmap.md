为了能够把若干张赛图打包到同一个 .osz 中，需要：

1. 修改难度名 `[Metadata] -> Version`
2. 修改音频文件名并将其加入对应文件夹 `[General] -> AudioFilename`
3. 修改bg名并加入对应文件夹 `[Events]`
4. 修改标题为比赛轮次名称 `[Metadata] -> Title/TitleUnicode`

以上拟通过 `regex` 直接正则查找并修改实现，`slider` 库实在是没用明白。

文件夹名称需要和比赛轮次名称和每个 `.osu` 文件的标题保持一致，否则可能出现游戏内读取错误的情况。

