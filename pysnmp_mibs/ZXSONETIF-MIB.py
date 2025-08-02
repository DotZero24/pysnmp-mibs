_N='zxSonetVTIfIndex'
_M='localTiming'
_L='loopTiming'
_K='inwardLoop'
_J='lineLoop'
_I='deprecated'
_H='not-accessible'
_G='DisplayString'
_F='zxSonetIfIndex'
_E='ZXSONETIF-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention','TruthValue')
zxPwCTDM,=mibBuilder.importSymbols('ZTE-MASTER-MIB','zxPwCTDM')
zxSonetIfMIB=ModuleIdentity((1,3,6,1,4,1,3902,1015,1013,2,1,3))
_ZxSonetCfgTable_Object=MibTable
zxSonetCfgTable=_ZxSonetCfgTable_Object((1,3,6,1,4,1,3902,1015,1013,2,1,3,1))
if mibBuilder.loadTexts:zxSonetCfgTable.setStatus(_A)
_ZxSonetCfgEntry_Object=MibTableRow
zxSonetCfgEntry=_ZxSonetCfgEntry_Object((1,3,6,1,4,1,3902,1015,1013,2,1,3,1,1))
zxSonetCfgEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxSonetCfgEntry.setStatus(_A)
_ZxSonetIfIndex_Type=InterfaceIndex
_ZxSonetIfIndex_Object=MibTableColumn
zxSonetIfIndex=_ZxSonetIfIndex_Object((1,3,6,1,4,1,3902,1015,1013,2,1,3,1,1,1),_ZxSonetIfIndex_Type())
zxSonetIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:zxSonetIfIndex.setStatus(_I)
class _ZxSonetLoopBackType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noLoopback',1),(_J,2),(_K,3)))
_ZxSonetLoopBackType_Type.__name__=_B
_ZxSonetLoopBackType_Object=MibTableColumn
zxSonetLoopBackType=_ZxSonetLoopBackType_Object((1,3,6,1,4,1,3902,1015,1013,2,1,3,1,1,2),_ZxSonetLoopBackType_Type())
zxSonetLoopBackType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxSonetLoopBackType.setStatus(_A)
class _ZxSonetClockSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_ZxSonetClockSource_Type.__name__=_B
_ZxSonetClockSource_Object=MibTableColumn
zxSonetClockSource=_ZxSonetClockSource_Object((1,3,6,1,4,1,3902,1015,1013,2,1,3,1,1,3),_ZxSonetClockSource_Type())
zxSonetClockSource.setMaxAccess(_C)
if mibBuilder.loadTexts:zxSonetClockSource.setStatus(_A)
class _ZxSonetConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('sonetSts3c',1),('sonetStm1',2),('sonetSts12c',3),('sonetStm4',4),('sonetSts48c',5),('sonetStm16',6),('sonetSts192c',7),('sonetStm64',8)))
_ZxSonetConfigType_Type.__name__=_B
_ZxSonetConfigType_Object=MibTableColumn
zxSonetConfigType=_ZxSonetConfigType_Object((1,3,6,1,4,1,3902,1015,1013,2,1,3,1,1,4),_ZxSonetConfigType_Type())
zxSonetConfigType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxSonetConfigType.setStatus(_A)
class _ZxSonetConfigMapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('other',0),('au3tu11',1),('au3tu12',2),('au4tu11',3),('au4tu12',4)))
_ZxSonetConfigMapType_Type.__name__=_B
_ZxSonetConfigMapType_Object=MibTableColumn
zxSonetConfigMapType=_ZxSonetConfigMapType_Object((1,3,6,1,4,1,3902,1015,1013,2,1,3,1,1,5),_ZxSonetConfigMapType_Type())
zxSonetConfigMapType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxSonetConfigMapType.setStatus(_A)
_ZxSonetCfgInfoSend_Type=TruthValue
_ZxSonetCfgInfoSend_Object=MibTableColumn
zxSonetCfgInfoSend=_ZxSonetCfgInfoSend_Object((1,3,6,1,4,1,3902,1015,1013,2,1,3,1,1,6),_ZxSonetCfgInfoSend_Type())
zxSonetCfgInfoSend.setMaxAccess(_C)
if mibBuilder.loadTexts:zxSonetCfgInfoSend.setStatus(_A)
_ZxSonetMediumTable_Object=MibTable
zxSonetMediumTable=_ZxSonetMediumTable_Object((1,3,6,1,4,1,3902,1015,1013,2,1,3,2))
if mibBuilder.loadTexts:zxSonetMediumTable.setStatus(_A)
_ZxSonetMediumEntry_Object=MibTableRow
zxSonetMediumEntry=_ZxSonetMediumEntry_Object((1,3,6,1,4,1,3902,1015,1013,2,1,3,2,1))
zxSonetMediumEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zxSonetMediumEntry.setStatus(_A)
class _ZxSonetMediumType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sonet',1),('sdh',2)))
_ZxSonetMediumType_Type.__name__=_B
_ZxSonetMediumType_Object=MibTableColumn
zxSonetMediumType=_ZxSonetMediumType_Object((1,3,6,1,4,1,3902,1015,1013,2,1,3,2,1,1),_ZxSonetMediumType_Type())
zxSonetMediumType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxSonetMediumType.setStatus(_A)
class _ZxSonetMediumTimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,900))
_ZxSonetMediumTimeElapsed_Type.__name__=_B
_ZxSonetMediumTimeElapsed_Object=MibTableColumn
zxSonetMediumTimeElapsed=_ZxSonetMediumTimeElapsed_Object((1,3,6,1,4,1,3902,1015,1013,2,1,3,2,1,2),_ZxSonetMediumTimeElapsed_Type())
zxSonetMediumTimeElapsed.setMaxAccess(_D)
if mibBuilder.loadTexts:zxSonetMediumTimeElapsed.setStatus(_A)
class _ZxSonetMediumValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_ZxSonetMediumValidIntervals_Type.__name__=_B
_ZxSonetMediumValidIntervals_Object=MibTableColumn
zxSonetMediumValidIntervals=_ZxSonetMediumValidIntervals_Object((1,3,6,1,4,1,3902,1015,1013,2,1,3,2,1,3),_ZxSonetMediumValidIntervals_Type())
zxSonetMediumValidIntervals.setMaxAccess(_D)
if mibBuilder.loadTexts:zxSonetMediumValidIntervals.setStatus(_A)
class _ZxSonetMediumLineCoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('sonetMediumOther',1),('sonetMediumB3ZS',2),('sonetMediumCMI',3),('sonetMediumNRZ',4),('sonetMediumRZ',5)))
_ZxSonetMediumLineCoding_Type.__name__=_B
_ZxSonetMediumLineCoding_Object=MibTableColumn
zxSonetMediumLineCoding=_ZxSonetMediumLineCoding_Object((1,3,6,1,4,1,3902,1015,1013,2,1,3,2,1,4),_ZxSonetMediumLineCoding_Type())
zxSonetMediumLineCoding.setMaxAccess(_C)
if mibBuilder.loadTexts:zxSonetMediumLineCoding.setStatus(_A)
class _ZxSonetMediumLineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('sonetOther',1),('sonetShortSingleMode',2),('sonetLongSingleMode',3),('sonetMultiMode',4),('sonetCoax',5),('sonetUTP',6)))
_ZxSonetMediumLineType_Type.__name__=_B
_ZxSonetMediumLineType_Object=MibTableColumn
zxSonetMediumLineType=_ZxSonetMediumLineType_Object((1,3,6,1,4,1,3902,1015,1013,2,1,3,2,1,5),_ZxSonetMediumLineType_Type())
zxSonetMediumLineType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxSonetMediumLineType.setStatus(_A)
class _ZxSonetMediumCircuitIdentifier_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ZxSonetMediumCircuitIdentifier_Type.__name__=_G
_ZxSonetMediumCircuitIdentifier_Object=MibTableColumn
zxSonetMediumCircuitIdentifier=_ZxSonetMediumCircuitIdentifier_Object((1,3,6,1,4,1,3902,1015,1013,2,1,3,2,1,6),_ZxSonetMediumCircuitIdentifier_Type())
zxSonetMediumCircuitIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:zxSonetMediumCircuitIdentifier.setStatus(_A)
class _ZxSonetMediumInvalidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_ZxSonetMediumInvalidIntervals_Type.__name__=_B
_ZxSonetMediumInvalidIntervals_Object=MibTableColumn
zxSonetMediumInvalidIntervals=_ZxSonetMediumInvalidIntervals_Object((1,3,6,1,4,1,3902,1015,1013,2,1,3,2,1,7),_ZxSonetMediumInvalidIntervals_Type())
zxSonetMediumInvalidIntervals.setMaxAccess(_D)
if mibBuilder.loadTexts:zxSonetMediumInvalidIntervals.setStatus(_A)
class _ZxSonetMediumLoopbackConfig_Type(Bits):namedValues=NamedValues(*(('sonetNoLoop',0),('sonetFacilityLoop',1),('sonetTerminalLoop',2),('sonetOtherLoop',3)))
_ZxSonetMediumLoopbackConfig_Type.__name__='Bits'
_ZxSonetMediumLoopbackConfig_Object=MibTableColumn
zxSonetMediumLoopbackConfig=_ZxSonetMediumLoopbackConfig_Object((1,3,6,1,4,1,3902,1015,1013,2,1,3,2,1,8),_ZxSonetMediumLoopbackConfig_Type())
zxSonetMediumLoopbackConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:zxSonetMediumLoopbackConfig.setStatus(_A)
_ZxSonetVTConfigTable_Object=MibTable
zxSonetVTConfigTable=_ZxSonetVTConfigTable_Object((1,3,6,1,4,1,3902,1015,1013,2,1,3,3))
if mibBuilder.loadTexts:zxSonetVTConfigTable.setStatus(_A)
_ZxSonetVTConfigEntry_Object=MibTableRow
zxSonetVTConfigEntry=_ZxSonetVTConfigEntry_Object((1,3,6,1,4,1,3902,1015,1013,2,1,3,3,1))
zxSonetVTConfigEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:zxSonetVTConfigEntry.setStatus(_A)
_ZxSonetVTIfIndex_Type=InterfaceIndex
_ZxSonetVTIfIndex_Object=MibTableColumn
zxSonetVTIfIndex=_ZxSonetVTIfIndex_Object((1,3,6,1,4,1,3902,1015,1013,2,1,3,3,1,1),_ZxSonetVTIfIndex_Type())
zxSonetVTIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:zxSonetVTIfIndex.setStatus(_I)
class _ZxSonetVTLoopbackConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('noLoop',1),('payloadLoop',2),(_J,3),('otherLoop',4),(_K,5),('dualLoop',6)))
_ZxSonetVTLoopbackConfig_Type.__name__=_B
_ZxSonetVTLoopbackConfig_Object=MibTableColumn
zxSonetVTLoopbackConfig=_ZxSonetVTLoopbackConfig_Object((1,3,6,1,4,1,3902,1015,1013,2,1,3,3,1,2),_ZxSonetVTLoopbackConfig_Type())
zxSonetVTLoopbackConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:zxSonetVTLoopbackConfig.setStatus(_A)
class _ZxSonetVTTransmitClockSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_L,1),(_M,2),('throughTiming',3),('adaptive',4),('enhancedAdaptive',5),('differential',6)))
_ZxSonetVTTransmitClockSource_Type.__name__=_B
_ZxSonetVTTransmitClockSource_Object=MibTableColumn
zxSonetVTTransmitClockSource=_ZxSonetVTTransmitClockSource_Object((1,3,6,1,4,1,3902,1015,1013,2,1,3,3,1,3),_ZxSonetVTTransmitClockSource_Type())
zxSonetVTTransmitClockSource.setMaxAccess(_C)
if mibBuilder.loadTexts:zxSonetVTTransmitClockSource.setStatus(_A)
class _ZxSonetVTClockStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_ZxSonetVTClockStatus_Type.__name__=_B
_ZxSonetVTClockStatus_Object=MibTableColumn
zxSonetVTClockStatus=_ZxSonetVTClockStatus_Object((1,3,6,1,4,1,3902,1015,1013,2,1,3,3,1,4),_ZxSonetVTClockStatus_Type())
zxSonetVTClockStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxSonetVTClockStatus.setStatus(_A)
_ZxSonetVTCfgInfoSend_Type=TruthValue
_ZxSonetVTCfgInfoSend_Object=MibTableColumn
zxSonetVTCfgInfoSend=_ZxSonetVTCfgInfoSend_Object((1,3,6,1,4,1,3902,1015,1013,2,1,3,3,1,5),_ZxSonetVTCfgInfoSend_Type())
zxSonetVTCfgInfoSend.setMaxAccess(_C)
if mibBuilder.loadTexts:zxSonetVTCfgInfoSend.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'zxSonetIfMIB':zxSonetIfMIB,'zxSonetCfgTable':zxSonetCfgTable,'zxSonetCfgEntry':zxSonetCfgEntry,_F:zxSonetIfIndex,'zxSonetLoopBackType':zxSonetLoopBackType,'zxSonetClockSource':zxSonetClockSource,'zxSonetConfigType':zxSonetConfigType,'zxSonetConfigMapType':zxSonetConfigMapType,'zxSonetCfgInfoSend':zxSonetCfgInfoSend,'zxSonetMediumTable':zxSonetMediumTable,'zxSonetMediumEntry':zxSonetMediumEntry,'zxSonetMediumType':zxSonetMediumType,'zxSonetMediumTimeElapsed':zxSonetMediumTimeElapsed,'zxSonetMediumValidIntervals':zxSonetMediumValidIntervals,'zxSonetMediumLineCoding':zxSonetMediumLineCoding,'zxSonetMediumLineType':zxSonetMediumLineType,'zxSonetMediumCircuitIdentifier':zxSonetMediumCircuitIdentifier,'zxSonetMediumInvalidIntervals':zxSonetMediumInvalidIntervals,'zxSonetMediumLoopbackConfig':zxSonetMediumLoopbackConfig,'zxSonetVTConfigTable':zxSonetVTConfigTable,'zxSonetVTConfigEntry':zxSonetVTConfigEntry,_N:zxSonetVTIfIndex,'zxSonetVTLoopbackConfig':zxSonetVTLoopbackConfig,'zxSonetVTTransmitClockSource':zxSonetVTTransmitClockSource,'zxSonetVTClockStatus':zxSonetVTClockStatus,'zxSonetVTCfgInfoSend':zxSonetVTCfgInfoSend})