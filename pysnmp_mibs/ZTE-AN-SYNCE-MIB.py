_H='zxAnSyncENniPortIndex'
_G='ZTE-AN-SYNCE-MIB'
_F='read-only'
_E='disable'
_D='enable'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ZxAnIfindex,zxAn=mibBuilder.importSymbols('ZTE-AN-TC-MIB','ZxAnIfindex','zxAn')
zxAnSyncEMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,65))
_ZxAnSyncEObjects_ObjectIdentity=ObjectIdentity
zxAnSyncEObjects=_ZxAnSyncEObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,65,1))
_ZxAnSyncEGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnSyncEGlobalObjects=_ZxAnSyncEGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,65,1,1))
class _ZxAnSyncEClockSourceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('localClock',1),('gps1pps',2),('pon8k',3),('clockRecovery',4)))
_ZxAnSyncEClockSourceType_Type.__name__=_B
_ZxAnSyncEClockSourceType_Object=MibScalar
zxAnSyncEClockSourceType=_ZxAnSyncEClockSourceType_Object((1,3,6,1,4,1,3902,1015,65,1,1,1),_ZxAnSyncEClockSourceType_Type())
zxAnSyncEClockSourceType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSyncEClockSourceType.setStatus(_A)
_ZxAnSyncEClockRecoveryPort_Type=ZxAnIfindex
_ZxAnSyncEClockRecoveryPort_Object=MibScalar
zxAnSyncEClockRecoveryPort=_ZxAnSyncEClockRecoveryPort_Object((1,3,6,1,4,1,3902,1015,65,1,1,2),_ZxAnSyncEClockRecoveryPort_Type())
zxAnSyncEClockRecoveryPort.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSyncEClockRecoveryPort.setStatus(_A)
class _ZxAnSyncEUniPortSyncEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ZxAnSyncEUniPortSyncEnable_Type.__name__=_B
_ZxAnSyncEUniPortSyncEnable_Object=MibScalar
zxAnSyncEUniPortSyncEnable=_ZxAnSyncEUniPortSyncEnable_Object((1,3,6,1,4,1,3902,1015,65,1,1,3),_ZxAnSyncEUniPortSyncEnable_Type())
zxAnSyncEUniPortSyncEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSyncEUniPortSyncEnable.setStatus(_A)
class _ZxAnSyncEClockSourceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_ZxAnSyncEClockSourceStatus_Type.__name__=_B
_ZxAnSyncEClockSourceStatus_Object=MibScalar
zxAnSyncEClockSourceStatus=_ZxAnSyncEClockSourceStatus_Object((1,3,6,1,4,1,3902,1015,65,1,1,4),_ZxAnSyncEClockSourceStatus_Type())
zxAnSyncEClockSourceStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnSyncEClockSourceStatus.setStatus(_A)
class _ZxAnSyncEClockOperationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,6,7,11,14,21,22,255)));namedValues=NamedValues(*(('freerunPhaselockedNormal',1),('holdover',2),('locked',4),('prelocked2LostPhase',5),('prelocked',6),('lostPhase',7),('freerun2PhaselockedAbnormal',11),('directPass',14),('destroyFreerunOrHoldover',21),('acquiring',22),('unknown',255)))
_ZxAnSyncEClockOperationStatus_Type.__name__=_B
_ZxAnSyncEClockOperationStatus_Object=MibScalar
zxAnSyncEClockOperationStatus=_ZxAnSyncEClockOperationStatus_Object((1,3,6,1,4,1,3902,1015,65,1,1,5),_ZxAnSyncEClockOperationStatus_Type())
zxAnSyncEClockOperationStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnSyncEClockOperationStatus.setStatus(_A)
_ZxAnSyncENniPortTable_Object=MibTable
zxAnSyncENniPortTable=_ZxAnSyncENniPortTable_Object((1,3,6,1,4,1,3902,1015,65,1,2))
if mibBuilder.loadTexts:zxAnSyncENniPortTable.setStatus(_A)
_ZxAnSyncENniPortEntry_Object=MibTableRow
zxAnSyncENniPortEntry=_ZxAnSyncENniPortEntry_Object((1,3,6,1,4,1,3902,1015,65,1,2,1))
zxAnSyncENniPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:zxAnSyncENniPortEntry.setStatus(_A)
_ZxAnSyncENniPortIndex_Type=ZxAnIfindex
_ZxAnSyncENniPortIndex_Object=MibTableColumn
zxAnSyncENniPortIndex=_ZxAnSyncENniPortIndex_Object((1,3,6,1,4,1,3902,1015,65,1,2,1,1),_ZxAnSyncENniPortIndex_Type())
zxAnSyncENniPortIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zxAnSyncENniPortIndex.setStatus(_A)
class _ZxAnSyncENniPortSyncEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_ZxAnSyncENniPortSyncEnable_Type.__name__=_B
_ZxAnSyncENniPortSyncEnable_Object=MibTableColumn
zxAnSyncENniPortSyncEnable=_ZxAnSyncENniPortSyncEnable_Object((1,3,6,1,4,1,3902,1015,65,1,2,1,2),_ZxAnSyncENniPortSyncEnable_Type())
zxAnSyncENniPortSyncEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSyncENniPortSyncEnable.setStatus(_A)
class _ZxAnSyncENniPortClockMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('master',1),('slave',2)))
_ZxAnSyncENniPortClockMode_Type.__name__=_B
_ZxAnSyncENniPortClockMode_Object=MibTableColumn
zxAnSyncENniPortClockMode=_ZxAnSyncENniPortClockMode_Object((1,3,6,1,4,1,3902,1015,65,1,2,1,3),_ZxAnSyncENniPortClockMode_Type())
zxAnSyncENniPortClockMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSyncENniPortClockMode.setStatus(_A)
_ZxAnSyncETrapObjects_ObjectIdentity=ObjectIdentity
zxAnSyncETrapObjects=_ZxAnSyncETrapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,65,2))
mibBuilder.exportSymbols(_G,**{'zxAnSyncEMib':zxAnSyncEMib,'zxAnSyncEObjects':zxAnSyncEObjects,'zxAnSyncEGlobalObjects':zxAnSyncEGlobalObjects,'zxAnSyncEClockSourceType':zxAnSyncEClockSourceType,'zxAnSyncEClockRecoveryPort':zxAnSyncEClockRecoveryPort,'zxAnSyncEUniPortSyncEnable':zxAnSyncEUniPortSyncEnable,'zxAnSyncEClockSourceStatus':zxAnSyncEClockSourceStatus,'zxAnSyncEClockOperationStatus':zxAnSyncEClockOperationStatus,'zxAnSyncENniPortTable':zxAnSyncENniPortTable,'zxAnSyncENniPortEntry':zxAnSyncENniPortEntry,_H:zxAnSyncENniPortIndex,'zxAnSyncENniPortSyncEnable':zxAnSyncENniPortSyncEnable,'zxAnSyncENniPortClockMode':zxAnSyncENniPortClockMode,'zxAnSyncETrapObjects':zxAnSyncETrapObjects})