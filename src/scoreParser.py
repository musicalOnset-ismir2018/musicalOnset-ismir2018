# -*- coding: utf-8 -*-

import csv
import os
import re

def removePunctuation(char):
    assert(type(char) == str)
    if len(re.findall(r'[\u4e00-\u9fff]+', char)):
        char = re.sub(r"[%s]+" % puncChinese, "", char)
    return char

def writerowCsv(syllables,syllable_durations,bpm,writer,pinyins=None):
    for ii in range(len(syllables)):
        writer.writerow(['']+syllables[ii])
        if pinyins:
            writer.writerow(['']+pinyins[ii])
        writer.writerow([bpm[ii]]+syllable_durations[ii])

def writeCsv(scoreFilename, syllables, syllable_durations, bpm):
    """
    write csv scores
    :param scoreFilename:
    :param syllables:
    :param syllable_durations:
    :param bpm:
    :return:
    """
    if len(syllables):

        directory, _ = os.path.split(scoreFilename)
        if not os.path.exists(directory):
            os.makedirs(directory)

        export=open(scoreFilename, "wb")
        writer=csv.writer(export, delimiter=',')
        writerowCsv(syllables,syllable_durations,bpm,writer,None)
        export.close()

def writeCsvPinyinFromData(scoreFilenamePinyin, syllables, pinyins, syllable_durations, bpm):
    if len(syllables):
        export=open(scoreFilenamePinyin, "wb")
        writer=csv.writer(export, delimiter=',')
        writerowCsv(syllables,syllable_durations,bpm,writer,pinyins)
        export.close()

def writeCsvPinyin(scoreFilename, scoreFilenamePinyin):
    '''
    use this function to add pinyin to scoreFilename
    :param scoreFilename:
    :param scoreFilenamePinyin:
    :return:
    '''
    syllables,pinyins,syllable_durations,bpm = generatePinyin(scoreFilename)
    writeCsvPinyinFromData(scoreFilenamePinyin, syllables, pinyins, syllable_durations, bpm)
