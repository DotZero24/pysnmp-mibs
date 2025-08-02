_M='TruthValue'
_L='disable'
_K='enable'
_J='sonet'
_I='sdh'
_H='DisplayString'
_G='ifDescr'
_F='read-only'
_E='Integer32'
_D='ifIndex'
_C='IF-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifDescr,ifIndex=mibBuilder.importSymbols(_C,_G,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention',_M)
hpnicfPos=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,19))
if mibBuilder.loadTexts:hpnicfPos.setRevisions(('2013-10-10 17:00','2010-05-19 17:00','2007-07-19 17:00'))
_HpnicfPosMIBObjects_ObjectIdentity=ObjectIdentity
hpnicfPosMIBObjects=_HpnicfPosMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,19,1))
_HpnicfPosParamTable_Object=MibTable
hpnicfPosParamTable=_HpnicfPosParamTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1))
if mibBuilder.loadTexts:hpnicfPosParamTable.setStatus(_A)
_HpnicfPosParamTableEntry_Object=MibTableRow
hpnicfPosParamTableEntry=_HpnicfPosParamTableEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1))
hpnicfPosParamTableEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:hpnicfPosParamTableEntry.setStatus(_A)
class _HpnicfPosCRC_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('crc32',1),('crc16',2)))
_HpnicfPosCRC_Type.__name__=_E
_HpnicfPosCRC_Object=MibTableColumn
hpnicfPosCRC=_HpnicfPosCRC_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,1),_HpnicfPosCRC_Type())
hpnicfPosCRC.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosCRC.setStatus(_A)
_HpnicfPosMTU_Type=Integer32
_HpnicfPosMTU_Object=MibTableColumn
hpnicfPosMTU=_HpnicfPosMTU_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,2),_HpnicfPosMTU_Type())
hpnicfPosMTU.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosMTU.setStatus(_A)
class _HpnicfPosScramble_Type(TruthValue):defaultValue=1
_HpnicfPosScramble_Type.__name__=_M
_HpnicfPosScramble_Object=MibTableColumn
hpnicfPosScramble=_HpnicfPosScramble_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,3),_HpnicfPosScramble_Type())
hpnicfPosScramble.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosScramble.setStatus(_A)
class _HpnicfPosClockSource_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('system',1),('line',2)))
_HpnicfPosClockSource_Type.__name__=_E
_HpnicfPosClockSource_Object=MibTableColumn
hpnicfPosClockSource=_HpnicfPosClockSource_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,4),_HpnicfPosClockSource_Type())
hpnicfPosClockSource.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosClockSource.setStatus(_A)
class _HpnicfPosSdhFlagJ0_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_HpnicfPosSdhFlagJ0_Type.__name__=_H
_HpnicfPosSdhFlagJ0_Object=MibTableColumn
hpnicfPosSdhFlagJ0=_HpnicfPosSdhFlagJ0_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,5),_HpnicfPosSdhFlagJ0_Type())
hpnicfPosSdhFlagJ0.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosSdhFlagJ0.setStatus(_A)
class _HpnicfPosSdhFlagJ1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_HpnicfPosSdhFlagJ1_Type.__name__=_H
_HpnicfPosSdhFlagJ1_Object=MibTableColumn
hpnicfPosSdhFlagJ1=_HpnicfPosSdhFlagJ1_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,6),_HpnicfPosSdhFlagJ1_Type())
hpnicfPosSdhFlagJ1.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosSdhFlagJ1.setStatus(_A)
class _HpnicfPosSonetFlagJ0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfPosSonetFlagJ0_Type.__name__=_E
_HpnicfPosSonetFlagJ0_Object=MibTableColumn
hpnicfPosSonetFlagJ0=_HpnicfPosSonetFlagJ0_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,7),_HpnicfPosSonetFlagJ0_Type())
hpnicfPosSonetFlagJ0.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosSonetFlagJ0.setStatus(_A)
class _HpnicfPosSonetFlagJ1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,62))
_HpnicfPosSonetFlagJ1_Type.__name__=_H
_HpnicfPosSonetFlagJ1_Object=MibTableColumn
hpnicfPosSonetFlagJ1=_HpnicfPosSonetFlagJ1_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,8),_HpnicfPosSonetFlagJ1_Type())
hpnicfPosSonetFlagJ1.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosSonetFlagJ1.setStatus(_A)
class _HpnicfPosFlagC2_Type(Integer32):defaultValue=22;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfPosFlagC2_Type.__name__=_E
_HpnicfPosFlagC2_Object=MibTableColumn
hpnicfPosFlagC2=_HpnicfPosFlagC2_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,9),_HpnicfPosFlagC2_Type())
hpnicfPosFlagC2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosFlagC2.setStatus(_A)
class _HpnicfPosFrameType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_HpnicfPosFrameType_Type.__name__=_E
_HpnicfPosFrameType_Object=MibTableColumn
hpnicfPosFrameType=_HpnicfPosFrameType_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,10),_HpnicfPosFrameType_Type())
hpnicfPosFrameType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosFrameType.setStatus(_A)
class _HpnicfPosBindVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_HpnicfPosBindVlanId_Type.__name__=_E
_HpnicfPosBindVlanId_Object=MibTableColumn
hpnicfPosBindVlanId=_HpnicfPosBindVlanId_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,11),_HpnicfPosBindVlanId_Type())
hpnicfPosBindVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosBindVlanId.setStatus(_A)
class _HpnicfPosEncapsulation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ppp',1),('hdlc',2),('fr',3)))
_HpnicfPosEncapsulation_Type.__name__=_E
_HpnicfPosEncapsulation_Object=MibTableColumn
hpnicfPosEncapsulation=_HpnicfPosEncapsulation_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,12),_HpnicfPosEncapsulation_Type())
hpnicfPosEncapsulation.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosEncapsulation.setStatus(_A)
class _HpnicfPoskeepaliveTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_HpnicfPoskeepaliveTimeout_Type.__name__=_E
_HpnicfPoskeepaliveTimeout_Object=MibTableColumn
hpnicfPoskeepaliveTimeout=_HpnicfPoskeepaliveTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,13),_HpnicfPoskeepaliveTimeout_Type())
hpnicfPoskeepaliveTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPoskeepaliveTimeout.setStatus(_A)
class _HpnicfPosBERthresholdSF_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,9))
_HpnicfPosBERthresholdSF_Type.__name__=_E
_HpnicfPosBERthresholdSF_Object=MibTableColumn
hpnicfPosBERthresholdSF=_HpnicfPosBERthresholdSF_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,14),_HpnicfPosBERthresholdSF_Type())
hpnicfPosBERthresholdSF.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosBERthresholdSF.setStatus(_A)
class _HpnicfPosBERthresholdSD_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,9))
_HpnicfPosBERthresholdSD_Type.__name__=_E
_HpnicfPosBERthresholdSD_Object=MibTableColumn
hpnicfPosBERthresholdSD=_HpnicfPosBERthresholdSD_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,15),_HpnicfPosBERthresholdSD_Type())
hpnicfPosBERthresholdSD.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosBERthresholdSD.setStatus(_A)
_HpnicfPosB1Error_Type=Counter64
_HpnicfPosB1Error_Object=MibTableColumn
hpnicfPosB1Error=_HpnicfPosB1Error_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,16),_HpnicfPosB1Error_Type())
hpnicfPosB1Error.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPosB1Error.setStatus(_A)
_HpnicfPosB2Error_Type=Counter64
_HpnicfPosB2Error_Object=MibTableColumn
hpnicfPosB2Error=_HpnicfPosB2Error_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,17),_HpnicfPosB2Error_Type())
hpnicfPosB2Error.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPosB2Error.setStatus(_A)
_HpnicfPosB3Error_Type=Counter64
_HpnicfPosB3Error_Object=MibTableColumn
hpnicfPosB3Error=_HpnicfPosB3Error_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,18),_HpnicfPosB3Error_Type())
hpnicfPosB3Error.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPosB3Error.setStatus(_A)
_HpnicfPosM1Error_Type=Counter64
_HpnicfPosM1Error_Object=MibTableColumn
hpnicfPosM1Error=_HpnicfPosM1Error_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,19),_HpnicfPosM1Error_Type())
hpnicfPosM1Error.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPosM1Error.setStatus(_A)
_HpnicfPosG1Error_Type=Counter64
_HpnicfPosG1Error_Object=MibTableColumn
hpnicfPosG1Error=_HpnicfPosG1Error_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,20),_HpnicfPosG1Error_Type())
hpnicfPosG1Error.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPosG1Error.setStatus(_A)
class _HpnicfPosFlagJ0Type_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_HpnicfPosFlagJ0Type_Type.__name__=_E
_HpnicfPosFlagJ0Type_Object=MibTableColumn
hpnicfPosFlagJ0Type=_HpnicfPosFlagJ0Type_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,21),_HpnicfPosFlagJ0Type_Type())
hpnicfPosFlagJ0Type.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosFlagJ0Type.setStatus(_A)
class _HpnicfPosFlagJ1Type_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_HpnicfPosFlagJ1Type_Type.__name__=_E
_HpnicfPosFlagJ1Type_Object=MibTableColumn
hpnicfPosFlagJ1Type=_HpnicfPosFlagJ1Type_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,22),_HpnicfPosFlagJ1Type_Type())
hpnicfPosFlagJ1Type.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosFlagJ1Type.setStatus(_A)
class _HpnicfPosB1TCAThreshold_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,9))
_HpnicfPosB1TCAThreshold_Type.__name__=_E
_HpnicfPosB1TCAThreshold_Object=MibTableColumn
hpnicfPosB1TCAThreshold=_HpnicfPosB1TCAThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,23),_HpnicfPosB1TCAThreshold_Type())
hpnicfPosB1TCAThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosB1TCAThreshold.setStatus(_A)
class _HpnicfPosB2TCAThreshold_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,9))
_HpnicfPosB2TCAThreshold_Type.__name__=_E
_HpnicfPosB2TCAThreshold_Object=MibTableColumn
hpnicfPosB2TCAThreshold=_HpnicfPosB2TCAThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,24),_HpnicfPosB2TCAThreshold_Type())
hpnicfPosB2TCAThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosB2TCAThreshold.setStatus(_A)
class _HpnicfPosB3TCAThreshold_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,9))
_HpnicfPosB3TCAThreshold_Type.__name__=_E
_HpnicfPosB3TCAThreshold_Object=MibTableColumn
hpnicfPosB3TCAThreshold=_HpnicfPosB3TCAThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,25),_HpnicfPosB3TCAThreshold_Type())
hpnicfPosB3TCAThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosB3TCAThreshold.setStatus(_A)
class _HpnicfPosB1TCAEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_HpnicfPosB1TCAEnable_Type.__name__=_E
_HpnicfPosB1TCAEnable_Object=MibTableColumn
hpnicfPosB1TCAEnable=_HpnicfPosB1TCAEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,26),_HpnicfPosB1TCAEnable_Type())
hpnicfPosB1TCAEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosB1TCAEnable.setStatus(_A)
class _HpnicfPosB2TCAEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_HpnicfPosB2TCAEnable_Type.__name__=_E
_HpnicfPosB2TCAEnable_Object=MibTableColumn
hpnicfPosB2TCAEnable=_HpnicfPosB2TCAEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,27),_HpnicfPosB2TCAEnable_Type())
hpnicfPosB2TCAEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosB2TCAEnable.setStatus(_A)
class _HpnicfPosB3TCAEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_HpnicfPosB3TCAEnable_Type.__name__=_E
_HpnicfPosB3TCAEnable_Object=MibTableColumn
hpnicfPosB3TCAEnable=_HpnicfPosB3TCAEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,19,1,1,1,28),_HpnicfPosB3TCAEnable_Type())
hpnicfPosB3TCAEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPosB3TCAEnable.setStatus(_A)
_HpnicfPosMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
hpnicfPosMIBNotificationsPrefix=_HpnicfPosMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,19,2))
_HpnicfPosMIBNotifications_ObjectIdentity=ObjectIdentity
hpnicfPosMIBNotifications=_HpnicfPosMIBNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,19,2,0))
hpnicfPosLOSAlarm=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,19,2,0,1))
hpnicfPosLOSAlarm.setObjects((_C,_D))
if mibBuilder.loadTexts:hpnicfPosLOSAlarm.setStatus(_A)
hpnicfPosLOFAlarm=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,19,2,0,2))
hpnicfPosLOFAlarm.setObjects((_C,_D))
if mibBuilder.loadTexts:hpnicfPosLOFAlarm.setStatus(_A)
hpnicfPosOOFAlarm=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,19,2,0,3))
hpnicfPosOOFAlarm.setObjects((_C,_D))
if mibBuilder.loadTexts:hpnicfPosOOFAlarm.setStatus(_A)
hpnicfPosLAISAlarm=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,19,2,0,4))
hpnicfPosLAISAlarm.setObjects((_C,_D))
if mibBuilder.loadTexts:hpnicfPosLAISAlarm.setStatus(_A)
hpnicfPosLRDIAlarm=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,19,2,0,5))
hpnicfPosLRDIAlarm.setObjects((_C,_D))
if mibBuilder.loadTexts:hpnicfPosLRDIAlarm.setStatus(_A)
hpnicfPosPRDIAlarm=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,19,2,0,6))
hpnicfPosPRDIAlarm.setObjects((_C,_D))
if mibBuilder.loadTexts:hpnicfPosPRDIAlarm.setStatus(_A)
hpnicfPosPAISAlarm=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,19,2,0,7))
hpnicfPosPAISAlarm.setObjects((_C,_D))
if mibBuilder.loadTexts:hpnicfPosPAISAlarm.setStatus(_A)
hpnicfPosLOPAlarm=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,19,2,0,8))
hpnicfPosLOPAlarm.setObjects((_C,_D))
if mibBuilder.loadTexts:hpnicfPosLOPAlarm.setStatus(_A)
hpnicfPosSTIMAlarm=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,19,2,0,9))
hpnicfPosSTIMAlarm.setObjects((_C,_D))
if mibBuilder.loadTexts:hpnicfPosSTIMAlarm.setStatus(_A)
hpnicfPosPTIMAlarm=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,19,2,0,10))
hpnicfPosPTIMAlarm.setObjects((_C,_D))
if mibBuilder.loadTexts:hpnicfPosPTIMAlarm.setStatus(_A)
hpnicfPosPSLMAlarm=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,19,2,0,11))
hpnicfPosPSLMAlarm.setObjects((_C,_D))
if mibBuilder.loadTexts:hpnicfPosPSLMAlarm.setStatus(_A)
hpnicfPosLSDAlarm=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,19,2,0,12))
hpnicfPosLSDAlarm.setObjects((_C,_D))
if mibBuilder.loadTexts:hpnicfPosLSDAlarm.setStatus(_A)
hpnicfPosLSFAlarm=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,19,2,0,13))
hpnicfPosLSFAlarm.setObjects((_C,_D))
if mibBuilder.loadTexts:hpnicfPosLSFAlarm.setStatus(_A)
hpnicfPosNormalAlarm=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,19,2,0,14))
hpnicfPosNormalAlarm.setObjects((_C,_D))
if mibBuilder.loadTexts:hpnicfPosNormalAlarm.setStatus(_A)
hpnicfPosB1TCAlarm=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,19,2,0,15))
hpnicfPosB1TCAlarm.setObjects(*((_C,_D),(_C,_G)))
if mibBuilder.loadTexts:hpnicfPosB1TCAlarm.setStatus(_A)
hpnicfPosB2TCAlarm=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,19,2,0,16))
hpnicfPosB2TCAlarm.setObjects(*((_C,_D),(_C,_G)))
if mibBuilder.loadTexts:hpnicfPosB2TCAlarm.setStatus(_A)
hpnicfPosB3TCAlarm=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,19,2,0,17))
hpnicfPosB3TCAlarm.setObjects(*((_C,_D),(_C,_G)))
if mibBuilder.loadTexts:hpnicfPosB3TCAlarm.setStatus(_A)
mibBuilder.exportSymbols('HPN-ICF-PPP-OVER-SONET-MIB',**{'hpnicfPos':hpnicfPos,'hpnicfPosMIBObjects':hpnicfPosMIBObjects,'hpnicfPosParamTable':hpnicfPosParamTable,'hpnicfPosParamTableEntry':hpnicfPosParamTableEntry,'hpnicfPosCRC':hpnicfPosCRC,'hpnicfPosMTU':hpnicfPosMTU,'hpnicfPosScramble':hpnicfPosScramble,'hpnicfPosClockSource':hpnicfPosClockSource,'hpnicfPosSdhFlagJ0':hpnicfPosSdhFlagJ0,'hpnicfPosSdhFlagJ1':hpnicfPosSdhFlagJ1,'hpnicfPosSonetFlagJ0':hpnicfPosSonetFlagJ0,'hpnicfPosSonetFlagJ1':hpnicfPosSonetFlagJ1,'hpnicfPosFlagC2':hpnicfPosFlagC2,'hpnicfPosFrameType':hpnicfPosFrameType,'hpnicfPosBindVlanId':hpnicfPosBindVlanId,'hpnicfPosEncapsulation':hpnicfPosEncapsulation,'hpnicfPoskeepaliveTimeout':hpnicfPoskeepaliveTimeout,'hpnicfPosBERthresholdSF':hpnicfPosBERthresholdSF,'hpnicfPosBERthresholdSD':hpnicfPosBERthresholdSD,'hpnicfPosB1Error':hpnicfPosB1Error,'hpnicfPosB2Error':hpnicfPosB2Error,'hpnicfPosB3Error':hpnicfPosB3Error,'hpnicfPosM1Error':hpnicfPosM1Error,'hpnicfPosG1Error':hpnicfPosG1Error,'hpnicfPosFlagJ0Type':hpnicfPosFlagJ0Type,'hpnicfPosFlagJ1Type':hpnicfPosFlagJ1Type,'hpnicfPosB1TCAThreshold':hpnicfPosB1TCAThreshold,'hpnicfPosB2TCAThreshold':hpnicfPosB2TCAThreshold,'hpnicfPosB3TCAThreshold':hpnicfPosB3TCAThreshold,'hpnicfPosB1TCAEnable':hpnicfPosB1TCAEnable,'hpnicfPosB2TCAEnable':hpnicfPosB2TCAEnable,'hpnicfPosB3TCAEnable':hpnicfPosB3TCAEnable,'hpnicfPosMIBNotificationsPrefix':hpnicfPosMIBNotificationsPrefix,'hpnicfPosMIBNotifications':hpnicfPosMIBNotifications,'hpnicfPosLOSAlarm':hpnicfPosLOSAlarm,'hpnicfPosLOFAlarm':hpnicfPosLOFAlarm,'hpnicfPosOOFAlarm':hpnicfPosOOFAlarm,'hpnicfPosLAISAlarm':hpnicfPosLAISAlarm,'hpnicfPosLRDIAlarm':hpnicfPosLRDIAlarm,'hpnicfPosPRDIAlarm':hpnicfPosPRDIAlarm,'hpnicfPosPAISAlarm':hpnicfPosPAISAlarm,'hpnicfPosLOPAlarm':hpnicfPosLOPAlarm,'hpnicfPosSTIMAlarm':hpnicfPosSTIMAlarm,'hpnicfPosPTIMAlarm':hpnicfPosPTIMAlarm,'hpnicfPosPSLMAlarm':hpnicfPosPSLMAlarm,'hpnicfPosLSDAlarm':hpnicfPosLSDAlarm,'hpnicfPosLSFAlarm':hpnicfPosLSFAlarm,'hpnicfPosNormalAlarm':hpnicfPosNormalAlarm,'hpnicfPosB1TCAlarm':hpnicfPosB1TCAlarm,'hpnicfPosB2TCAlarm':hpnicfPosB2TCAlarm,'hpnicfPosB3TCAlarm':hpnicfPosB3TCAlarm})