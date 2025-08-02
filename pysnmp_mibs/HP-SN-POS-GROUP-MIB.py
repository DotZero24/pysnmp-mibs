_J='internal'
_I='testing'
_H='snPOSInfoPortNum'
_G='HP-SN-POS-GROUP-MIB'
_F='DisplayString'
_E='OctetString'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
snPOS,=mibBuilder.importSymbols('HP-SN-ROOT-MIB','snPOS')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
class POSStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
class DisplayString(OctetString):0
_SnPOSInfo_ObjectIdentity=ObjectIdentity
snPOSInfo=_SnPOSInfo_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1))
_SnPOSInfoTable_Object=MibTable
snPOSInfoTable=_SnPOSInfoTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1))
if mibBuilder.loadTexts:snPOSInfoTable.setStatus(_A)
_SnPOSInfoEntry_Object=MibTableRow
snPOSInfoEntry=_SnPOSInfoEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1))
snPOSInfoEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:snPOSInfoEntry.setStatus(_A)
_SnPOSInfoPortNum_Type=Integer32
_SnPOSInfoPortNum_Object=MibTableColumn
snPOSInfoPortNum=_SnPOSInfoPortNum_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,1),_SnPOSInfoPortNum_Type())
snPOSInfoPortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSInfoPortNum.setStatus(_A)
_SnPOSIfIndex_Type=Integer32
_SnPOSIfIndex_Object=MibTableColumn
snPOSIfIndex=_SnPOSIfIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,2),_SnPOSIfIndex_Type())
snPOSIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSIfIndex.setStatus(_A)
_SnPOSDescr_Type=DisplayString
_SnPOSDescr_Object=MibTableColumn
snPOSDescr=_SnPOSDescr_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,3),_SnPOSDescr_Type())
snPOSDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSDescr.setStatus(_A)
class _SnPOSName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SnPOSName_Type.__name__=_F
_SnPOSName_Object=MibTableColumn
snPOSName=_SnPOSName_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,4),_SnPOSName_Type())
snPOSName.setMaxAccess(_D)
if mibBuilder.loadTexts:snPOSName.setStatus(_A)
class _SnPOSInfoSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('s155000',1),('s622000',2),('other',3),('s2488000',4)))
_SnPOSInfoSpeed_Type.__name__=_C
_SnPOSInfoSpeed_Object=MibTableColumn
snPOSInfoSpeed=_SnPOSInfoSpeed_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,5),_SnPOSInfoSpeed_Type())
snPOSInfoSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:snPOSInfoSpeed.setStatus(_A)
class _SnPOSInfoAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_I,3)))
_SnPOSInfoAdminStatus_Type.__name__=_C
_SnPOSInfoAdminStatus_Object=MibTableColumn
snPOSInfoAdminStatus=_SnPOSInfoAdminStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,6),_SnPOSInfoAdminStatus_Type())
snPOSInfoAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:snPOSInfoAdminStatus.setStatus(_A)
class _SnPOSInfoLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_I,3)))
_SnPOSInfoLinkStatus_Type.__name__=_C
_SnPOSInfoLinkStatus_Object=MibTableColumn
snPOSInfoLinkStatus=_SnPOSInfoLinkStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,7),_SnPOSInfoLinkStatus_Type())
snPOSInfoLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSInfoLinkStatus.setStatus(_A)
class _SnPOSInfoClock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('line',2)))
_SnPOSInfoClock_Type.__name__=_C
_SnPOSInfoClock_Object=MibTableColumn
snPOSInfoClock=_SnPOSInfoClock_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,8),_SnPOSInfoClock_Type())
snPOSInfoClock.setMaxAccess(_D)
if mibBuilder.loadTexts:snPOSInfoClock.setStatus(_A)
class _SnPOSInfoLoopBack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('line',1),(_J,2),('none',3)))
_SnPOSInfoLoopBack_Type.__name__=_C
_SnPOSInfoLoopBack_Object=MibTableColumn
snPOSInfoLoopBack=_SnPOSInfoLoopBack_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,9),_SnPOSInfoLoopBack_Type())
snPOSInfoLoopBack.setMaxAccess(_D)
if mibBuilder.loadTexts:snPOSInfoLoopBack.setStatus(_A)
_SnPOSInfoScrambleATM_Type=POSStatus
_SnPOSInfoScrambleATM_Object=MibTableColumn
snPOSInfoScrambleATM=_SnPOSInfoScrambleATM_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,10),_SnPOSInfoScrambleATM_Type())
snPOSInfoScrambleATM.setMaxAccess(_D)
if mibBuilder.loadTexts:snPOSInfoScrambleATM.setStatus(_A)
class _SnPOSInfoFraming_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sonet',1),('sdh',2)))
_SnPOSInfoFraming_Type.__name__=_C
_SnPOSInfoFraming_Object=MibTableColumn
snPOSInfoFraming=_SnPOSInfoFraming_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,11),_SnPOSInfoFraming_Type())
snPOSInfoFraming.setMaxAccess(_D)
if mibBuilder.loadTexts:snPOSInfoFraming.setStatus(_A)
class _SnPOSInfoCRC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('crc32bits',1),('crc16bits',2)))
_SnPOSInfoCRC_Type.__name__=_C
_SnPOSInfoCRC_Object=MibTableColumn
snPOSInfoCRC=_SnPOSInfoCRC_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,12),_SnPOSInfoCRC_Type())
snPOSInfoCRC.setMaxAccess(_D)
if mibBuilder.loadTexts:snPOSInfoCRC.setStatus(_A)
class _SnPOSInfoKeepAlive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_SnPOSInfoKeepAlive_Type.__name__=_C
_SnPOSInfoKeepAlive_Object=MibTableColumn
snPOSInfoKeepAlive=_SnPOSInfoKeepAlive_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,13),_SnPOSInfoKeepAlive_Type())
snPOSInfoKeepAlive.setMaxAccess(_D)
if mibBuilder.loadTexts:snPOSInfoKeepAlive.setStatus(_A)
class _SnPOSInfoFlagC2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnPOSInfoFlagC2_Type.__name__=_C
_SnPOSInfoFlagC2_Object=MibTableColumn
snPOSInfoFlagC2=_SnPOSInfoFlagC2_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,14),_SnPOSInfoFlagC2_Type())
snPOSInfoFlagC2.setMaxAccess(_D)
if mibBuilder.loadTexts:snPOSInfoFlagC2.setStatus(_A)
class _SnPOSInfoFlagJ0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnPOSInfoFlagJ0_Type.__name__=_C
_SnPOSInfoFlagJ0_Object=MibTableColumn
snPOSInfoFlagJ0=_SnPOSInfoFlagJ0_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,15),_SnPOSInfoFlagJ0_Type())
snPOSInfoFlagJ0.setMaxAccess(_D)
if mibBuilder.loadTexts:snPOSInfoFlagJ0.setStatus(_A)
class _SnPOSInfoFlagH1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnPOSInfoFlagH1_Type.__name__=_C
_SnPOSInfoFlagH1_Object=MibTableColumn
snPOSInfoFlagH1=_SnPOSInfoFlagH1_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,16),_SnPOSInfoFlagH1_Type())
snPOSInfoFlagH1.setMaxAccess(_D)
if mibBuilder.loadTexts:snPOSInfoFlagH1.setStatus(_A)
_SnPOSStatsInFrames_Type=Counter32
_SnPOSStatsInFrames_Object=MibTableColumn
snPOSStatsInFrames=_SnPOSStatsInFrames_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,17),_SnPOSStatsInFrames_Type())
snPOSStatsInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsInFrames.setStatus(_A)
_SnPOSStatsOutFrames_Type=Counter32
_SnPOSStatsOutFrames_Object=MibTableColumn
snPOSStatsOutFrames=_SnPOSStatsOutFrames_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,18),_SnPOSStatsOutFrames_Type())
snPOSStatsOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsOutFrames.setStatus(_A)
_SnPOSStatsAlignErrors_Type=Counter32
_SnPOSStatsAlignErrors_Object=MibTableColumn
snPOSStatsAlignErrors=_SnPOSStatsAlignErrors_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,19),_SnPOSStatsAlignErrors_Type())
snPOSStatsAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsAlignErrors.setStatus(_A)
_SnPOSStatsFCSErrors_Type=Counter32
_SnPOSStatsFCSErrors_Object=MibTableColumn
snPOSStatsFCSErrors=_SnPOSStatsFCSErrors_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,20),_SnPOSStatsFCSErrors_Type())
snPOSStatsFCSErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsFCSErrors.setStatus(_A)
_SnPOSStatsFrameTooLongs_Type=Counter32
_SnPOSStatsFrameTooLongs_Object=MibTableColumn
snPOSStatsFrameTooLongs=_SnPOSStatsFrameTooLongs_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,21),_SnPOSStatsFrameTooLongs_Type())
snPOSStatsFrameTooLongs.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsFrameTooLongs.setStatus(_A)
_SnPOSStatsFrameTooShorts_Type=Counter32
_SnPOSStatsFrameTooShorts_Object=MibTableColumn
snPOSStatsFrameTooShorts=_SnPOSStatsFrameTooShorts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,22),_SnPOSStatsFrameTooShorts_Type())
snPOSStatsFrameTooShorts.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsFrameTooShorts.setStatus(_A)
_SnPOSStatsInDiscard_Type=Counter32
_SnPOSStatsInDiscard_Object=MibTableColumn
snPOSStatsInDiscard=_SnPOSStatsInDiscard_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,23),_SnPOSStatsInDiscard_Type())
snPOSStatsInDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsInDiscard.setStatus(_A)
_SnPOSStatsOutDiscard_Type=Counter32
_SnPOSStatsOutDiscard_Object=MibTableColumn
snPOSStatsOutDiscard=_SnPOSStatsOutDiscard_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,24),_SnPOSStatsOutDiscard_Type())
snPOSStatsOutDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsOutDiscard.setStatus(_A)
class _SnPOSInOctets_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SnPOSInOctets_Type.__name__=_E
_SnPOSInOctets_Object=MibTableColumn
snPOSInOctets=_SnPOSInOctets_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,25),_SnPOSInOctets_Type())
snPOSInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSInOctets.setStatus(_A)
class _SnPOSOutOctets_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SnPOSOutOctets_Type.__name__=_E
_SnPOSOutOctets_Object=MibTableColumn
snPOSOutOctets=_SnPOSOutOctets_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,26),_SnPOSOutOctets_Type())
snPOSOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSOutOctets.setStatus(_A)
_SnPOSStatsInBitsPerSec_Type=Gauge32
_SnPOSStatsInBitsPerSec_Object=MibTableColumn
snPOSStatsInBitsPerSec=_SnPOSStatsInBitsPerSec_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,27),_SnPOSStatsInBitsPerSec_Type())
snPOSStatsInBitsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsInBitsPerSec.setStatus(_A)
_SnPOSStatsOutBitsPerSec_Type=Gauge32
_SnPOSStatsOutBitsPerSec_Object=MibTableColumn
snPOSStatsOutBitsPerSec=_SnPOSStatsOutBitsPerSec_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,28),_SnPOSStatsOutBitsPerSec_Type())
snPOSStatsOutBitsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsOutBitsPerSec.setStatus(_A)
_SnPOSStatsInPktsPerSec_Type=Gauge32
_SnPOSStatsInPktsPerSec_Object=MibTableColumn
snPOSStatsInPktsPerSec=_SnPOSStatsInPktsPerSec_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,29),_SnPOSStatsInPktsPerSec_Type())
snPOSStatsInPktsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsInPktsPerSec.setStatus(_A)
_SnPOSStatsOutPktsPerSec_Type=Gauge32
_SnPOSStatsOutPktsPerSec_Object=MibTableColumn
snPOSStatsOutPktsPerSec=_SnPOSStatsOutPktsPerSec_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,30),_SnPOSStatsOutPktsPerSec_Type())
snPOSStatsOutPktsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsOutPktsPerSec.setStatus(_A)
class _SnPOSStatsInUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_SnPOSStatsInUtilization_Type.__name__=_C
_SnPOSStatsInUtilization_Object=MibTableColumn
snPOSStatsInUtilization=_SnPOSStatsInUtilization_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,31),_SnPOSStatsInUtilization_Type())
snPOSStatsInUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsInUtilization.setStatus(_A)
class _SnPOSStatsOutUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_SnPOSStatsOutUtilization_Type.__name__=_C
_SnPOSStatsOutUtilization_Object=MibTableColumn
snPOSStatsOutUtilization=_SnPOSStatsOutUtilization_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,32),_SnPOSStatsOutUtilization_Type())
snPOSStatsOutUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsOutUtilization.setStatus(_A)
class _SnPOSTagType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tagged',1),('untagged',2)))
_SnPOSTagType_Type.__name__=_C
_SnPOSTagType_Object=MibTableColumn
snPOSTagType=_SnPOSTagType_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,33),_SnPOSTagType_Type())
snPOSTagType.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSTagType.setStatus(_A)
_SnPOSStatsB1_Type=Counter32
_SnPOSStatsB1_Object=MibTableColumn
snPOSStatsB1=_SnPOSStatsB1_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,34),_SnPOSStatsB1_Type())
snPOSStatsB1.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsB1.setStatus(_A)
_SnPOSStatsB2_Type=Counter32
_SnPOSStatsB2_Object=MibTableColumn
snPOSStatsB2=_SnPOSStatsB2_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,35),_SnPOSStatsB2_Type())
snPOSStatsB2.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsB2.setStatus(_A)
_SnPOSStatsB3_Type=Counter32
_SnPOSStatsB3_Object=MibTableColumn
snPOSStatsB3=_SnPOSStatsB3_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,36),_SnPOSStatsB3_Type())
snPOSStatsB3.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsB3.setStatus(_A)
_SnPOSStatsAIS_Type=Counter32
_SnPOSStatsAIS_Object=MibTableColumn
snPOSStatsAIS=_SnPOSStatsAIS_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,37),_SnPOSStatsAIS_Type())
snPOSStatsAIS.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsAIS.setStatus(_A)
_SnPOSStatsRDI_Type=Counter32
_SnPOSStatsRDI_Object=MibTableColumn
snPOSStatsRDI=_SnPOSStatsRDI_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,38),_SnPOSStatsRDI_Type())
snPOSStatsRDI.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsRDI.setStatus(_A)
_SnPOSStatsLOP_Type=Counter32
_SnPOSStatsLOP_Object=MibTableColumn
snPOSStatsLOP=_SnPOSStatsLOP_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,39),_SnPOSStatsLOP_Type())
snPOSStatsLOP.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsLOP.setStatus(_A)
_SnPOSStatsLOF_Type=Counter32
_SnPOSStatsLOF_Object=MibTableColumn
snPOSStatsLOF=_SnPOSStatsLOF_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,40),_SnPOSStatsLOF_Type())
snPOSStatsLOF.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsLOF.setStatus(_A)
_SnPOSStatsLOS_Type=Counter32
_SnPOSStatsLOS_Object=MibTableColumn
snPOSStatsLOS=_SnPOSStatsLOS_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,14,1,1,1,41),_SnPOSStatsLOS_Type())
snPOSStatsLOS.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsLOS.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'POSStatus':POSStatus,_F:DisplayString,'snPOSInfo':snPOSInfo,'snPOSInfoTable':snPOSInfoTable,'snPOSInfoEntry':snPOSInfoEntry,_H:snPOSInfoPortNum,'snPOSIfIndex':snPOSIfIndex,'snPOSDescr':snPOSDescr,'snPOSName':snPOSName,'snPOSInfoSpeed':snPOSInfoSpeed,'snPOSInfoAdminStatus':snPOSInfoAdminStatus,'snPOSInfoLinkStatus':snPOSInfoLinkStatus,'snPOSInfoClock':snPOSInfoClock,'snPOSInfoLoopBack':snPOSInfoLoopBack,'snPOSInfoScrambleATM':snPOSInfoScrambleATM,'snPOSInfoFraming':snPOSInfoFraming,'snPOSInfoCRC':snPOSInfoCRC,'snPOSInfoKeepAlive':snPOSInfoKeepAlive,'snPOSInfoFlagC2':snPOSInfoFlagC2,'snPOSInfoFlagJ0':snPOSInfoFlagJ0,'snPOSInfoFlagH1':snPOSInfoFlagH1,'snPOSStatsInFrames':snPOSStatsInFrames,'snPOSStatsOutFrames':snPOSStatsOutFrames,'snPOSStatsAlignErrors':snPOSStatsAlignErrors,'snPOSStatsFCSErrors':snPOSStatsFCSErrors,'snPOSStatsFrameTooLongs':snPOSStatsFrameTooLongs,'snPOSStatsFrameTooShorts':snPOSStatsFrameTooShorts,'snPOSStatsInDiscard':snPOSStatsInDiscard,'snPOSStatsOutDiscard':snPOSStatsOutDiscard,'snPOSInOctets':snPOSInOctets,'snPOSOutOctets':snPOSOutOctets,'snPOSStatsInBitsPerSec':snPOSStatsInBitsPerSec,'snPOSStatsOutBitsPerSec':snPOSStatsOutBitsPerSec,'snPOSStatsInPktsPerSec':snPOSStatsInPktsPerSec,'snPOSStatsOutPktsPerSec':snPOSStatsOutPktsPerSec,'snPOSStatsInUtilization':snPOSStatsInUtilization,'snPOSStatsOutUtilization':snPOSStatsOutUtilization,'snPOSTagType':snPOSTagType,'snPOSStatsB1':snPOSStatsB1,'snPOSStatsB2':snPOSStatsB2,'snPOSStatsB3':snPOSStatsB3,'snPOSStatsAIS':snPOSStatsAIS,'snPOSStatsRDI':snPOSStatsRDI,'snPOSStatsLOP':snPOSStatsLOP,'snPOSStatsLOF':snPOSStatsLOF,'snPOSStatsLOS':snPOSStatsLOS})