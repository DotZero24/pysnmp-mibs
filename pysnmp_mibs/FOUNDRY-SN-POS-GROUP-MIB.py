_S='unknown'
_R='POSStatus'
_Q='crc16bits'
_P='crc32bits'
_O='testing'
_N='snPOSInfoPortNum'
_M='FOUNDRY-SN-POS-GROUP-MIB'
_L='line'
_K='internal'
_J='down'
_I='Unsigned32'
_H='ifIndex'
_G='IF-MIB'
_F='DisplayString'
_E='OctetString'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
router,=mibBuilder.importSymbols('FOUNDRY-SN-ROOT-MIB','router')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
snPOS=ModuleIdentity((1,3,6,1,4,1,1991,1,2,14))
if mibBuilder.loadTexts:snPOS.setRevisions(('2009-09-30 00:00','2017-08-07 00:00'))
class POSStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_SnPOSInfo_ObjectIdentity=ObjectIdentity
snPOSInfo=_SnPOSInfo_ObjectIdentity((1,3,6,1,4,1,1991,1,2,14,1))
_SnPOSInfoTable_Object=MibTable
snPOSInfoTable=_SnPOSInfoTable_Object((1,3,6,1,4,1,1991,1,2,14,1,1))
if mibBuilder.loadTexts:snPOSInfoTable.setStatus(_A)
_SnPOSInfoEntry_Object=MibTableRow
snPOSInfoEntry=_SnPOSInfoEntry_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1))
snPOSInfoEntry.setIndexNames((0,_M,_N))
if mibBuilder.loadTexts:snPOSInfoEntry.setStatus(_A)
_SnPOSInfoPortNum_Type=Integer32
_SnPOSInfoPortNum_Object=MibTableColumn
snPOSInfoPortNum=_SnPOSInfoPortNum_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,1),_SnPOSInfoPortNum_Type())
snPOSInfoPortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSInfoPortNum.setStatus(_A)
_SnPOSIfIndex_Type=Integer32
_SnPOSIfIndex_Object=MibTableColumn
snPOSIfIndex=_SnPOSIfIndex_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,2),_SnPOSIfIndex_Type())
snPOSIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSIfIndex.setStatus(_A)
_SnPOSDescr_Type=DisplayString
_SnPOSDescr_Object=MibTableColumn
snPOSDescr=_SnPOSDescr_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,3),_SnPOSDescr_Type())
snPOSDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSDescr.setStatus(_A)
class _SnPOSName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SnPOSName_Type.__name__=_F
_SnPOSName_Object=MibTableColumn
snPOSName=_SnPOSName_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,4),_SnPOSName_Type())
snPOSName.setMaxAccess(_C)
if mibBuilder.loadTexts:snPOSName.setStatus(_A)
class _SnPOSInfoSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('s155000',1),('s622000',2),('other',3),('s2488000',4)))
_SnPOSInfoSpeed_Type.__name__=_D
_SnPOSInfoSpeed_Object=MibTableColumn
snPOSInfoSpeed=_SnPOSInfoSpeed_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,5),_SnPOSInfoSpeed_Type())
snPOSInfoSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:snPOSInfoSpeed.setStatus(_A)
class _SnPOSInfoAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),(_J,2),(_O,3)))
_SnPOSInfoAdminStatus_Type.__name__=_D
_SnPOSInfoAdminStatus_Object=MibTableColumn
snPOSInfoAdminStatus=_SnPOSInfoAdminStatus_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,6),_SnPOSInfoAdminStatus_Type())
snPOSInfoAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:snPOSInfoAdminStatus.setStatus(_A)
class _SnPOSInfoLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),(_J,2),(_O,3)))
_SnPOSInfoLinkStatus_Type.__name__=_D
_SnPOSInfoLinkStatus_Object=MibTableColumn
snPOSInfoLinkStatus=_SnPOSInfoLinkStatus_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,7),_SnPOSInfoLinkStatus_Type())
snPOSInfoLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSInfoLinkStatus.setStatus(_A)
class _SnPOSInfoClock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_SnPOSInfoClock_Type.__name__=_D
_SnPOSInfoClock_Object=MibTableColumn
snPOSInfoClock=_SnPOSInfoClock_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,8),_SnPOSInfoClock_Type())
snPOSInfoClock.setMaxAccess(_C)
if mibBuilder.loadTexts:snPOSInfoClock.setStatus(_A)
class _SnPOSInfoLoopBack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_K,2),('none',3)))
_SnPOSInfoLoopBack_Type.__name__=_D
_SnPOSInfoLoopBack_Object=MibTableColumn
snPOSInfoLoopBack=_SnPOSInfoLoopBack_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,9),_SnPOSInfoLoopBack_Type())
snPOSInfoLoopBack.setMaxAccess(_C)
if mibBuilder.loadTexts:snPOSInfoLoopBack.setStatus(_A)
_SnPOSInfoScrambleATM_Type=POSStatus
_SnPOSInfoScrambleATM_Object=MibTableColumn
snPOSInfoScrambleATM=_SnPOSInfoScrambleATM_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,10),_SnPOSInfoScrambleATM_Type())
snPOSInfoScrambleATM.setMaxAccess(_C)
if mibBuilder.loadTexts:snPOSInfoScrambleATM.setStatus(_A)
class _SnPOSInfoFraming_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sonet',1),('sdh',2)))
_SnPOSInfoFraming_Type.__name__=_D
_SnPOSInfoFraming_Object=MibTableColumn
snPOSInfoFraming=_SnPOSInfoFraming_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,11),_SnPOSInfoFraming_Type())
snPOSInfoFraming.setMaxAccess(_C)
if mibBuilder.loadTexts:snPOSInfoFraming.setStatus(_A)
class _SnPOSInfoCRC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_SnPOSInfoCRC_Type.__name__=_D
_SnPOSInfoCRC_Object=MibTableColumn
snPOSInfoCRC=_SnPOSInfoCRC_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,12),_SnPOSInfoCRC_Type())
snPOSInfoCRC.setMaxAccess(_C)
if mibBuilder.loadTexts:snPOSInfoCRC.setStatus(_A)
class _SnPOSInfoKeepAlive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_SnPOSInfoKeepAlive_Type.__name__=_D
_SnPOSInfoKeepAlive_Object=MibTableColumn
snPOSInfoKeepAlive=_SnPOSInfoKeepAlive_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,13),_SnPOSInfoKeepAlive_Type())
snPOSInfoKeepAlive.setMaxAccess(_C)
if mibBuilder.loadTexts:snPOSInfoKeepAlive.setStatus(_A)
class _SnPOSInfoFlagC2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnPOSInfoFlagC2_Type.__name__=_D
_SnPOSInfoFlagC2_Object=MibTableColumn
snPOSInfoFlagC2=_SnPOSInfoFlagC2_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,14),_SnPOSInfoFlagC2_Type())
snPOSInfoFlagC2.setMaxAccess(_C)
if mibBuilder.loadTexts:snPOSInfoFlagC2.setStatus(_A)
class _SnPOSInfoFlagJ0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnPOSInfoFlagJ0_Type.__name__=_D
_SnPOSInfoFlagJ0_Object=MibTableColumn
snPOSInfoFlagJ0=_SnPOSInfoFlagJ0_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,15),_SnPOSInfoFlagJ0_Type())
snPOSInfoFlagJ0.setMaxAccess(_C)
if mibBuilder.loadTexts:snPOSInfoFlagJ0.setStatus(_A)
class _SnPOSInfoFlagH1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnPOSInfoFlagH1_Type.__name__=_D
_SnPOSInfoFlagH1_Object=MibTableColumn
snPOSInfoFlagH1=_SnPOSInfoFlagH1_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,16),_SnPOSInfoFlagH1_Type())
snPOSInfoFlagH1.setMaxAccess(_C)
if mibBuilder.loadTexts:snPOSInfoFlagH1.setStatus(_A)
_SnPOSStatsInFrames_Type=Counter32
_SnPOSStatsInFrames_Object=MibTableColumn
snPOSStatsInFrames=_SnPOSStatsInFrames_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,17),_SnPOSStatsInFrames_Type())
snPOSStatsInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsInFrames.setStatus(_A)
_SnPOSStatsOutFrames_Type=Counter32
_SnPOSStatsOutFrames_Object=MibTableColumn
snPOSStatsOutFrames=_SnPOSStatsOutFrames_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,18),_SnPOSStatsOutFrames_Type())
snPOSStatsOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsOutFrames.setStatus(_A)
_SnPOSStatsAlignErrors_Type=Counter32
_SnPOSStatsAlignErrors_Object=MibTableColumn
snPOSStatsAlignErrors=_SnPOSStatsAlignErrors_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,19),_SnPOSStatsAlignErrors_Type())
snPOSStatsAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsAlignErrors.setStatus(_A)
_SnPOSStatsFCSErrors_Type=Counter32
_SnPOSStatsFCSErrors_Object=MibTableColumn
snPOSStatsFCSErrors=_SnPOSStatsFCSErrors_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,20),_SnPOSStatsFCSErrors_Type())
snPOSStatsFCSErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsFCSErrors.setStatus(_A)
_SnPOSStatsFrameTooLongs_Type=Counter32
_SnPOSStatsFrameTooLongs_Object=MibTableColumn
snPOSStatsFrameTooLongs=_SnPOSStatsFrameTooLongs_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,21),_SnPOSStatsFrameTooLongs_Type())
snPOSStatsFrameTooLongs.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsFrameTooLongs.setStatus(_A)
_SnPOSStatsFrameTooShorts_Type=Counter32
_SnPOSStatsFrameTooShorts_Object=MibTableColumn
snPOSStatsFrameTooShorts=_SnPOSStatsFrameTooShorts_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,22),_SnPOSStatsFrameTooShorts_Type())
snPOSStatsFrameTooShorts.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsFrameTooShorts.setStatus(_A)
_SnPOSStatsInDiscard_Type=Counter32
_SnPOSStatsInDiscard_Object=MibTableColumn
snPOSStatsInDiscard=_SnPOSStatsInDiscard_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,23),_SnPOSStatsInDiscard_Type())
snPOSStatsInDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsInDiscard.setStatus(_A)
_SnPOSStatsOutDiscard_Type=Counter32
_SnPOSStatsOutDiscard_Object=MibTableColumn
snPOSStatsOutDiscard=_SnPOSStatsOutDiscard_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,24),_SnPOSStatsOutDiscard_Type())
snPOSStatsOutDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsOutDiscard.setStatus(_A)
class _SnPOSInOctets_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SnPOSInOctets_Type.__name__=_E
_SnPOSInOctets_Object=MibTableColumn
snPOSInOctets=_SnPOSInOctets_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,25),_SnPOSInOctets_Type())
snPOSInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSInOctets.setStatus(_A)
class _SnPOSOutOctets_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SnPOSOutOctets_Type.__name__=_E
_SnPOSOutOctets_Object=MibTableColumn
snPOSOutOctets=_SnPOSOutOctets_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,26),_SnPOSOutOctets_Type())
snPOSOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSOutOctets.setStatus(_A)
_SnPOSStatsInBitsPerSec_Type=Gauge32
_SnPOSStatsInBitsPerSec_Object=MibTableColumn
snPOSStatsInBitsPerSec=_SnPOSStatsInBitsPerSec_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,27),_SnPOSStatsInBitsPerSec_Type())
snPOSStatsInBitsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsInBitsPerSec.setStatus(_A)
_SnPOSStatsOutBitsPerSec_Type=Gauge32
_SnPOSStatsOutBitsPerSec_Object=MibTableColumn
snPOSStatsOutBitsPerSec=_SnPOSStatsOutBitsPerSec_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,28),_SnPOSStatsOutBitsPerSec_Type())
snPOSStatsOutBitsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsOutBitsPerSec.setStatus(_A)
_SnPOSStatsInPktsPerSec_Type=Gauge32
_SnPOSStatsInPktsPerSec_Object=MibTableColumn
snPOSStatsInPktsPerSec=_SnPOSStatsInPktsPerSec_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,29),_SnPOSStatsInPktsPerSec_Type())
snPOSStatsInPktsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsInPktsPerSec.setStatus(_A)
_SnPOSStatsOutPktsPerSec_Type=Gauge32
_SnPOSStatsOutPktsPerSec_Object=MibTableColumn
snPOSStatsOutPktsPerSec=_SnPOSStatsOutPktsPerSec_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,30),_SnPOSStatsOutPktsPerSec_Type())
snPOSStatsOutPktsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsOutPktsPerSec.setStatus(_A)
class _SnPOSStatsInUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_SnPOSStatsInUtilization_Type.__name__=_D
_SnPOSStatsInUtilization_Object=MibTableColumn
snPOSStatsInUtilization=_SnPOSStatsInUtilization_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,31),_SnPOSStatsInUtilization_Type())
snPOSStatsInUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsInUtilization.setStatus(_A)
class _SnPOSStatsOutUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_SnPOSStatsOutUtilization_Type.__name__=_D
_SnPOSStatsOutUtilization_Object=MibTableColumn
snPOSStatsOutUtilization=_SnPOSStatsOutUtilization_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,32),_SnPOSStatsOutUtilization_Type())
snPOSStatsOutUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsOutUtilization.setStatus(_A)
class _SnPOSTagType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tagged',1),('untagged',2)))
_SnPOSTagType_Type.__name__=_D
_SnPOSTagType_Object=MibTableColumn
snPOSTagType=_SnPOSTagType_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,33),_SnPOSTagType_Type())
snPOSTagType.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSTagType.setStatus(_A)
_SnPOSStatsB1_Type=Counter32
_SnPOSStatsB1_Object=MibTableColumn
snPOSStatsB1=_SnPOSStatsB1_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,34),_SnPOSStatsB1_Type())
snPOSStatsB1.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsB1.setStatus(_A)
_SnPOSStatsB2_Type=Counter32
_SnPOSStatsB2_Object=MibTableColumn
snPOSStatsB2=_SnPOSStatsB2_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,35),_SnPOSStatsB2_Type())
snPOSStatsB2.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsB2.setStatus(_A)
_SnPOSStatsB3_Type=Counter32
_SnPOSStatsB3_Object=MibTableColumn
snPOSStatsB3=_SnPOSStatsB3_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,36),_SnPOSStatsB3_Type())
snPOSStatsB3.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsB3.setStatus(_A)
_SnPOSStatsAIS_Type=Counter32
_SnPOSStatsAIS_Object=MibTableColumn
snPOSStatsAIS=_SnPOSStatsAIS_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,37),_SnPOSStatsAIS_Type())
snPOSStatsAIS.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsAIS.setStatus(_A)
_SnPOSStatsRDI_Type=Counter32
_SnPOSStatsRDI_Object=MibTableColumn
snPOSStatsRDI=_SnPOSStatsRDI_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,38),_SnPOSStatsRDI_Type())
snPOSStatsRDI.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsRDI.setStatus(_A)
_SnPOSStatsLOP_Type=Counter32
_SnPOSStatsLOP_Object=MibTableColumn
snPOSStatsLOP=_SnPOSStatsLOP_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,39),_SnPOSStatsLOP_Type())
snPOSStatsLOP.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsLOP.setStatus(_A)
_SnPOSStatsLOF_Type=Counter32
_SnPOSStatsLOF_Object=MibTableColumn
snPOSStatsLOF=_SnPOSStatsLOF_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,40),_SnPOSStatsLOF_Type())
snPOSStatsLOF.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsLOF.setStatus(_A)
_SnPOSStatsLOS_Type=Counter32
_SnPOSStatsLOS_Object=MibTableColumn
snPOSStatsLOS=_SnPOSStatsLOS_Object((1,3,6,1,4,1,1991,1,2,14,1,1,1,41),_SnPOSStatsLOS_Type())
snPOSStatsLOS.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOSStatsLOS.setStatus(_A)
_SnPOSInfo2Table_Object=MibTable
snPOSInfo2Table=_SnPOSInfo2Table_Object((1,3,6,1,4,1,1991,1,2,14,1,2))
if mibBuilder.loadTexts:snPOSInfo2Table.setStatus(_A)
_SnPOSInfo2Entry_Object=MibTableRow
snPOSInfo2Entry=_SnPOSInfo2Entry_Object((1,3,6,1,4,1,1991,1,2,14,1,2,1))
snPOSInfo2Entry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:snPOSInfo2Entry.setStatus(_A)
class _SnPOSInfo2Clock_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_SnPOSInfo2Clock_Type.__name__=_D
_SnPOSInfo2Clock_Object=MibTableColumn
snPOSInfo2Clock=_SnPOSInfo2Clock_Object((1,3,6,1,4,1,1991,1,2,14,1,2,1,1),_SnPOSInfo2Clock_Type())
snPOSInfo2Clock.setMaxAccess(_C)
if mibBuilder.loadTexts:snPOSInfo2Clock.setStatus(_A)
class _SnPOSInfo2ScrambleATM_Type(POSStatus):defaultValue=0
_SnPOSInfo2ScrambleATM_Type.__name__=_R
_SnPOSInfo2ScrambleATM_Object=MibTableColumn
snPOSInfo2ScrambleATM=_SnPOSInfo2ScrambleATM_Object((1,3,6,1,4,1,1991,1,2,14,1,2,1,2),_SnPOSInfo2ScrambleATM_Type())
snPOSInfo2ScrambleATM.setMaxAccess(_C)
if mibBuilder.loadTexts:snPOSInfo2ScrambleATM.setStatus(_A)
class _SnPOSInfo2CRC_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_SnPOSInfo2CRC_Type.__name__=_D
_SnPOSInfo2CRC_Object=MibTableColumn
snPOSInfo2CRC=_SnPOSInfo2CRC_Object((1,3,6,1,4,1,1991,1,2,14,1,2,1,3),_SnPOSInfo2CRC_Type())
snPOSInfo2CRC.setMaxAccess(_C)
if mibBuilder.loadTexts:snPOSInfo2CRC.setStatus(_A)
class _SnPOSInfo2KeepAlive_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnPOSInfo2KeepAlive_Type.__name__=_I
_SnPOSInfo2KeepAlive_Object=MibTableColumn
snPOSInfo2KeepAlive=_SnPOSInfo2KeepAlive_Object((1,3,6,1,4,1,1991,1,2,14,1,2,1,4),_SnPOSInfo2KeepAlive_Type())
snPOSInfo2KeepAlive.setMaxAccess(_C)
if mibBuilder.loadTexts:snPOSInfo2KeepAlive.setStatus(_A)
class _SnPOSInfo2FlagC2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnPOSInfo2FlagC2_Type.__name__=_I
_SnPOSInfo2FlagC2_Object=MibTableColumn
snPOSInfo2FlagC2=_SnPOSInfo2FlagC2_Object((1,3,6,1,4,1,1991,1,2,14,1,2,1,5),_SnPOSInfo2FlagC2_Type())
snPOSInfo2FlagC2.setMaxAccess(_C)
if mibBuilder.loadTexts:snPOSInfo2FlagC2.setStatus(_A)
class _SnPOSInfo2SSM_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('t1SonetPrimaryReferenceSource',1),('t1SonetTraceabilityUnknown',2),('t1SonetStratum2Traceable',3),('t1SonetTransitNodeClock',4),('t1SonetStratum3eTraceable',5),('t1SonetStratum3Traceable',6),('t1SonetMinClockTraceable',7),('t1SonetDus',8),('e1SdhTraceabilityUnknown',9),('e1SdhSsmTransitNodeClockG812',10),('e1SdhDus',11),('e1SdhSsmPrimaryReferenceClockG811',12),('e1SdhSsmLocalG812',13),('e1SdhSsmSyncEquipmentTimingSource',14)))
_SnPOSInfo2SSM_Type.__name__=_D
_SnPOSInfo2SSM_Object=MibTableColumn
snPOSInfo2SSM=_SnPOSInfo2SSM_Object((1,3,6,1,4,1,1991,1,2,14,1,2,1,6),_SnPOSInfo2SSM_Type())
snPOSInfo2SSM.setMaxAccess(_C)
if mibBuilder.loadTexts:snPOSInfo2SSM.setStatus(_A)
class _SnPOSInfo2Encapsulation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ppp',1),('hdlc',2)))
_SnPOSInfo2Encapsulation_Type.__name__=_D
_SnPOSInfo2Encapsulation_Object=MibTableColumn
snPOSInfo2Encapsulation=_SnPOSInfo2Encapsulation_Object((1,3,6,1,4,1,1991,1,2,14,1,2,1,7),_SnPOSInfo2Encapsulation_Type())
snPOSInfo2Encapsulation.setMaxAccess(_C)
if mibBuilder.loadTexts:snPOSInfo2Encapsulation.setStatus(_A)
class _SnPOSInfo2AlarmMonitoring_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_SnPOSInfo2AlarmMonitoring_Type.__name__=_D
_SnPOSInfo2AlarmMonitoring_Object=MibTableColumn
snPOSInfo2AlarmMonitoring=_SnPOSInfo2AlarmMonitoring_Object((1,3,6,1,4,1,1991,1,2,14,1,2,1,8),_SnPOSInfo2AlarmMonitoring_Type())
snPOSInfo2AlarmMonitoring.setMaxAccess(_C)
if mibBuilder.loadTexts:snPOSInfo2AlarmMonitoring.setStatus(_A)
class _SnPOSInfo2OverheadJ0ExpectedMessage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_SnPOSInfo2OverheadJ0ExpectedMessage_Type.__name__=_E
_SnPOSInfo2OverheadJ0ExpectedMessage_Object=MibTableColumn
snPOSInfo2OverheadJ0ExpectedMessage=_SnPOSInfo2OverheadJ0ExpectedMessage_Object((1,3,6,1,4,1,1991,1,2,14,1,2,1,9),_SnPOSInfo2OverheadJ0ExpectedMessage_Type())
snPOSInfo2OverheadJ0ExpectedMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:snPOSInfo2OverheadJ0ExpectedMessage.setStatus(_A)
class _SnPOSInfo2OverheadJ0TransmitMessage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_SnPOSInfo2OverheadJ0TransmitMessage_Type.__name__=_E
_SnPOSInfo2OverheadJ0TransmitMessage_Object=MibTableColumn
snPOSInfo2OverheadJ0TransmitMessage=_SnPOSInfo2OverheadJ0TransmitMessage_Object((1,3,6,1,4,1,1991,1,2,14,1,2,1,10),_SnPOSInfo2OverheadJ0TransmitMessage_Type())
snPOSInfo2OverheadJ0TransmitMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:snPOSInfo2OverheadJ0TransmitMessage.setStatus(_A)
class _SnPOSInfo2OverheadJ1ExpectedMessage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,64))
_SnPOSInfo2OverheadJ1ExpectedMessage_Type.__name__=_E
_SnPOSInfo2OverheadJ1ExpectedMessage_Object=MibTableColumn
snPOSInfo2OverheadJ1ExpectedMessage=_SnPOSInfo2OverheadJ1ExpectedMessage_Object((1,3,6,1,4,1,1991,1,2,14,1,2,1,11),_SnPOSInfo2OverheadJ1ExpectedMessage_Type())
snPOSInfo2OverheadJ1ExpectedMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:snPOSInfo2OverheadJ1ExpectedMessage.setStatus(_A)
class _SnPOSInfo2OverheadJ1MessageLength_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(16,64)));namedValues=NamedValues(*(('s16',16),('s64',64)))
_SnPOSInfo2OverheadJ1MessageLength_Type.__name__=_D
_SnPOSInfo2OverheadJ1MessageLength_Object=MibTableColumn
snPOSInfo2OverheadJ1MessageLength=_SnPOSInfo2OverheadJ1MessageLength_Object((1,3,6,1,4,1,1991,1,2,14,1,2,1,12),_SnPOSInfo2OverheadJ1MessageLength_Type())
snPOSInfo2OverheadJ1MessageLength.setMaxAccess(_C)
if mibBuilder.loadTexts:snPOSInfo2OverheadJ1MessageLength.setStatus(_A)
class _SnPOSInfo2OverheadJ1TransmitMessage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,64))
_SnPOSInfo2OverheadJ1TransmitMessage_Type.__name__=_E
_SnPOSInfo2OverheadJ1TransmitMessage_Object=MibTableColumn
snPOSInfo2OverheadJ1TransmitMessage=_SnPOSInfo2OverheadJ1TransmitMessage_Object((1,3,6,1,4,1,1991,1,2,14,1,2,1,13),_SnPOSInfo2OverheadJ1TransmitMessage_Type())
snPOSInfo2OverheadJ1TransmitMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:snPOSInfo2OverheadJ1TransmitMessage.setStatus(_A)
_SnPOSPPPTable_Object=MibTable
snPOSPPPTable=_SnPOSPPPTable_Object((1,3,6,1,4,1,1991,1,2,14,1,3))
if mibBuilder.loadTexts:snPOSPPPTable.setStatus(_A)
_SnPOSPPPEntry_Object=MibTableRow
snPOSPPPEntry=_SnPOSPPPEntry_Object((1,3,6,1,4,1,1991,1,2,14,1,3,1))
snPOSPPPEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:snPOSPPPEntry.setStatus(_A)
class _SnPosPppLcp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnPosPppLcp_Type.__name__=_F
_SnPosPppLcp_Object=MibTableColumn
snPosPppLcp=_SnPosPppLcp_Object((1,3,6,1,4,1,1991,1,2,14,1,3,1,1),_SnPosPppLcp_Type())
snPosPppLcp.setMaxAccess(_B)
if mibBuilder.loadTexts:snPosPppLcp.setStatus(_A)
class _SnPosPppIpCp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnPosPppIpCp_Type.__name__=_F
_SnPosPppIpCp_Object=MibTableColumn
snPosPppIpCp=_SnPosPppIpCp_Object((1,3,6,1,4,1,1991,1,2,14,1,3,1,2),_SnPosPppIpCp_Type())
snPosPppIpCp.setMaxAccess(_B)
if mibBuilder.loadTexts:snPosPppIpCp.setStatus(_A)
class _SnPosPppIpv6Cp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnPosPppIpv6Cp_Type.__name__=_F
_SnPosPppIpv6Cp_Object=MibTableColumn
snPosPppIpv6Cp=_SnPosPppIpv6Cp_Object((1,3,6,1,4,1,1991,1,2,14,1,3,1,3),_SnPosPppIpv6Cp_Type())
snPosPppIpv6Cp.setMaxAccess(_B)
if mibBuilder.loadTexts:snPosPppIpv6Cp.setStatus(_A)
class _SnPosPppOsInLcp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnPosPppOsInLcp_Type.__name__=_F
_SnPosPppOsInLcp_Object=MibTableColumn
snPosPppOsInLcp=_SnPosPppOsInLcp_Object((1,3,6,1,4,1,1991,1,2,14,1,3,1,4),_SnPosPppOsInLcp_Type())
snPosPppOsInLcp.setMaxAccess(_B)
if mibBuilder.loadTexts:snPosPppOsInLcp.setStatus(_A)
class _SnPosPppMpLscp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnPosPppMpLscp_Type.__name__=_F
_SnPosPppMpLscp_Object=MibTableColumn
snPosPppMpLscp=_SnPosPppMpLscp_Object((1,3,6,1,4,1,1991,1,2,14,1,3,1,5),_SnPosPppMpLscp_Type())
snPosPppMpLscp.setMaxAccess(_B)
if mibBuilder.loadTexts:snPosPppMpLscp.setStatus(_A)
_SnPOScHDLCTable_Object=MibTable
snPOScHDLCTable=_SnPOScHDLCTable_Object((1,3,6,1,4,1,1991,1,2,14,1,4))
if mibBuilder.loadTexts:snPOScHDLCTable.setStatus(_A)
_SnPOScHDLCEntry_Object=MibTableRow
snPOScHDLCEntry=_SnPOScHDLCEntry_Object((1,3,6,1,4,1,1991,1,2,14,1,4,1))
snPOScHDLCEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:snPOScHDLCEntry.setStatus(_A)
class _SnPOScHDLCLineState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('up',1),(_S,2)))
_SnPOScHDLCLineState_Type.__name__=_D
_SnPOScHDLCLineState_Object=MibTableColumn
snPOScHDLCLineState=_SnPOScHDLCLineState_Object((1,3,6,1,4,1,1991,1,2,14,1,4,1,1),_SnPOScHDLCLineState_Type())
snPOScHDLCLineState.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOScHDLCLineState.setStatus(_A)
class _SnPOScHDLCInLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('no',0),('yes',1),(_S,2)))
_SnPOScHDLCInLoopback_Type.__name__=_D
_SnPOScHDLCInLoopback_Object=MibTableColumn
snPOScHDLCInLoopback=_SnPOScHDLCInLoopback_Object((1,3,6,1,4,1,1991,1,2,14,1,4,1,2),_SnPOScHDLCInLoopback_Type())
snPOScHDLCInLoopback.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOScHDLCInLoopback.setStatus(_A)
_SnPOScHDLCMySeq_Type=Unsigned32
_SnPOScHDLCMySeq_Object=MibTableColumn
snPOScHDLCMySeq=_SnPOScHDLCMySeq_Object((1,3,6,1,4,1,1991,1,2,14,1,4,1,3),_SnPOScHDLCMySeq_Type())
snPOScHDLCMySeq.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOScHDLCMySeq.setStatus(_A)
_SnPOScHDLCMySeqSeen_Type=Unsigned32
_SnPOScHDLCMySeqSeen_Object=MibTableColumn
snPOScHDLCMySeqSeen=_SnPOScHDLCMySeqSeen_Object((1,3,6,1,4,1,1991,1,2,14,1,4,1,4),_SnPOScHDLCMySeqSeen_Type())
snPOScHDLCMySeqSeen.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOScHDLCMySeqSeen.setStatus(_A)
_SnPOScHDLCPeerSeqSeen_Type=Unsigned32
_SnPOScHDLCPeerSeqSeen_Object=MibTableColumn
snPOScHDLCPeerSeqSeen=_SnPOScHDLCPeerSeqSeen_Object((1,3,6,1,4,1,1991,1,2,14,1,4,1,5),_SnPOScHDLCPeerSeqSeen_Type())
snPOScHDLCPeerSeqSeen.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOScHDLCPeerSeqSeen.setStatus(_A)
_SnPOScHDLCUniqueSent_Type=Unsigned32
_SnPOScHDLCUniqueSent_Object=MibTableColumn
snPOScHDLCUniqueSent=_SnPOScHDLCUniqueSent_Object((1,3,6,1,4,1,1991,1,2,14,1,4,1,6),_SnPOScHDLCUniqueSent_Type())
snPOScHDLCUniqueSent.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOScHDLCUniqueSent.setStatus(_A)
_SnPOScHDLCUniqueReceived_Type=Unsigned32
_SnPOScHDLCUniqueReceived_Object=MibTableColumn
snPOScHDLCUniqueReceived=_SnPOScHDLCUniqueReceived_Object((1,3,6,1,4,1,1991,1,2,14,1,4,1,7),_SnPOScHDLCUniqueReceived_Type())
snPOScHDLCUniqueReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:snPOScHDLCUniqueReceived.setStatus(_A)
mibBuilder.exportSymbols(_M,**{_R:POSStatus,'snPOS':snPOS,'snPOSInfo':snPOSInfo,'snPOSInfoTable':snPOSInfoTable,'snPOSInfoEntry':snPOSInfoEntry,_N:snPOSInfoPortNum,'snPOSIfIndex':snPOSIfIndex,'snPOSDescr':snPOSDescr,'snPOSName':snPOSName,'snPOSInfoSpeed':snPOSInfoSpeed,'snPOSInfoAdminStatus':snPOSInfoAdminStatus,'snPOSInfoLinkStatus':snPOSInfoLinkStatus,'snPOSInfoClock':snPOSInfoClock,'snPOSInfoLoopBack':snPOSInfoLoopBack,'snPOSInfoScrambleATM':snPOSInfoScrambleATM,'snPOSInfoFraming':snPOSInfoFraming,'snPOSInfoCRC':snPOSInfoCRC,'snPOSInfoKeepAlive':snPOSInfoKeepAlive,'snPOSInfoFlagC2':snPOSInfoFlagC2,'snPOSInfoFlagJ0':snPOSInfoFlagJ0,'snPOSInfoFlagH1':snPOSInfoFlagH1,'snPOSStatsInFrames':snPOSStatsInFrames,'snPOSStatsOutFrames':snPOSStatsOutFrames,'snPOSStatsAlignErrors':snPOSStatsAlignErrors,'snPOSStatsFCSErrors':snPOSStatsFCSErrors,'snPOSStatsFrameTooLongs':snPOSStatsFrameTooLongs,'snPOSStatsFrameTooShorts':snPOSStatsFrameTooShorts,'snPOSStatsInDiscard':snPOSStatsInDiscard,'snPOSStatsOutDiscard':snPOSStatsOutDiscard,'snPOSInOctets':snPOSInOctets,'snPOSOutOctets':snPOSOutOctets,'snPOSStatsInBitsPerSec':snPOSStatsInBitsPerSec,'snPOSStatsOutBitsPerSec':snPOSStatsOutBitsPerSec,'snPOSStatsInPktsPerSec':snPOSStatsInPktsPerSec,'snPOSStatsOutPktsPerSec':snPOSStatsOutPktsPerSec,'snPOSStatsInUtilization':snPOSStatsInUtilization,'snPOSStatsOutUtilization':snPOSStatsOutUtilization,'snPOSTagType':snPOSTagType,'snPOSStatsB1':snPOSStatsB1,'snPOSStatsB2':snPOSStatsB2,'snPOSStatsB3':snPOSStatsB3,'snPOSStatsAIS':snPOSStatsAIS,'snPOSStatsRDI':snPOSStatsRDI,'snPOSStatsLOP':snPOSStatsLOP,'snPOSStatsLOF':snPOSStatsLOF,'snPOSStatsLOS':snPOSStatsLOS,'snPOSInfo2Table':snPOSInfo2Table,'snPOSInfo2Entry':snPOSInfo2Entry,'snPOSInfo2Clock':snPOSInfo2Clock,'snPOSInfo2ScrambleATM':snPOSInfo2ScrambleATM,'snPOSInfo2CRC':snPOSInfo2CRC,'snPOSInfo2KeepAlive':snPOSInfo2KeepAlive,'snPOSInfo2FlagC2':snPOSInfo2FlagC2,'snPOSInfo2SSM':snPOSInfo2SSM,'snPOSInfo2Encapsulation':snPOSInfo2Encapsulation,'snPOSInfo2AlarmMonitoring':snPOSInfo2AlarmMonitoring,'snPOSInfo2OverheadJ0ExpectedMessage':snPOSInfo2OverheadJ0ExpectedMessage,'snPOSInfo2OverheadJ0TransmitMessage':snPOSInfo2OverheadJ0TransmitMessage,'snPOSInfo2OverheadJ1ExpectedMessage':snPOSInfo2OverheadJ1ExpectedMessage,'snPOSInfo2OverheadJ1MessageLength':snPOSInfo2OverheadJ1MessageLength,'snPOSInfo2OverheadJ1TransmitMessage':snPOSInfo2OverheadJ1TransmitMessage,'snPOSPPPTable':snPOSPPPTable,'snPOSPPPEntry':snPOSPPPEntry,'snPosPppLcp':snPosPppLcp,'snPosPppIpCp':snPosPppIpCp,'snPosPppIpv6Cp':snPosPppIpv6Cp,'snPosPppOsInLcp':snPosPppOsInLcp,'snPosPppMpLscp':snPosPppMpLscp,'snPOScHDLCTable':snPOScHDLCTable,'snPOScHDLCEntry':snPOScHDLCEntry,'snPOScHDLCLineState':snPOScHDLCLineState,'snPOScHDLCInLoopback':snPOScHDLCInLoopback,'snPOScHDLCMySeq':snPOScHDLCMySeq,'snPOScHDLCMySeqSeen':snPOScHDLCMySeqSeen,'snPOScHDLCPeerSeqSeen':snPOScHDLCPeerSeqSeen,'snPOScHDLCUniqueSent':snPOScHDLCUniqueSent,'snPOScHDLCUniqueReceived':snPOScHDLCUniqueReceived})