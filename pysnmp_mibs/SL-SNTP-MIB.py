_J='slSntpConfigVariance'
_I='slSntpConfigMaxVariance'
_H='read-only'
_G='TruthValue'
_F='read-create'
_E='slSntpConfigAddress'
_D='SL-SNTP-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
slMain,=mibBuilder.importSymbols('SL-MAIN-MIB','slMain')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_G)
slSntp=ModuleIdentity((1,3,6,1,4,1,4515,1,3,21))
_SlSntpConfig_ObjectIdentity=ObjectIdentity
slSntpConfig=_SlSntpConfig_ObjectIdentity((1,3,6,1,4,1,4515,1,3,21,1))
class _SlSntpConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disabled',1),('unicast',2),('broadcast',3)))
_SlSntpConfigMode_Type.__name__=_B
_SlSntpConfigMode_Object=MibScalar
slSntpConfigMode=_SlSntpConfigMode_Object((1,3,6,1,4,1,4515,1,3,21,1,1),_SlSntpConfigMode_Type())
slSntpConfigMode.setMaxAccess(_C)
if mibBuilder.loadTexts:slSntpConfigMode.setStatus(_A)
class _SlSntpConfigPollInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,65535))
_SlSntpConfigPollInterval_Type.__name__=_B
_SlSntpConfigPollInterval_Object=MibScalar
slSntpConfigPollInterval=_SlSntpConfigPollInterval_Object((1,3,6,1,4,1,4515,1,3,21,1,2),_SlSntpConfigPollInterval_Type())
slSntpConfigPollInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:slSntpConfigPollInterval.setStatus(_A)
class _SlSntpConfigRetryCount_Type(Integer32):defaultValue=3
_SlSntpConfigRetryCount_Type.__name__=_B
_SlSntpConfigRetryCount_Object=MibScalar
slSntpConfigRetryCount=_SlSntpConfigRetryCount_Object((1,3,6,1,4,1,4515,1,3,21,1,3),_SlSntpConfigRetryCount_Type())
slSntpConfigRetryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:slSntpConfigRetryCount.setStatus(_A)
class _SlSntpConfigTimeZone_Type(Integer32):defaultValue=0
_SlSntpConfigTimeZone_Type.__name__=_B
_SlSntpConfigTimeZone_Object=MibScalar
slSntpConfigTimeZone=_SlSntpConfigTimeZone_Object((1,3,6,1,4,1,4515,1,3,21,1,4),_SlSntpConfigTimeZone_Type())
slSntpConfigTimeZone.setMaxAccess(_C)
if mibBuilder.loadTexts:slSntpConfigTimeZone.setStatus(_A)
class _SlSntpConfigDayLightSaving_Type(TruthValue):defaultValue=2
_SlSntpConfigDayLightSaving_Type.__name__=_G
_SlSntpConfigDayLightSaving_Object=MibScalar
slSntpConfigDayLightSaving=_SlSntpConfigDayLightSaving_Object((1,3,6,1,4,1,4515,1,3,21,1,5),_SlSntpConfigDayLightSaving_Type())
slSntpConfigDayLightSaving.setMaxAccess(_C)
if mibBuilder.loadTexts:slSntpConfigDayLightSaving.setStatus(_A)
class _SlSntpConfigFractTimeZone_Type(Integer32):defaultValue=0
_SlSntpConfigFractTimeZone_Type.__name__=_B
_SlSntpConfigFractTimeZone_Object=MibScalar
slSntpConfigFractTimeZone=_SlSntpConfigFractTimeZone_Object((1,3,6,1,4,1,4515,1,3,21,1,6),_SlSntpConfigFractTimeZone_Type())
slSntpConfigFractTimeZone.setMaxAccess(_C)
if mibBuilder.loadTexts:slSntpConfigFractTimeZone.setStatus(_A)
_SlSntpConfigTable_Object=MibTable
slSntpConfigTable=_SlSntpConfigTable_Object((1,3,6,1,4,1,4515,1,3,21,1,10))
if mibBuilder.loadTexts:slSntpConfigTable.setStatus(_A)
_SlSntpConfigEntry_Object=MibTableRow
slSntpConfigEntry=_SlSntpConfigEntry_Object((1,3,6,1,4,1,4515,1,3,21,1,10,1))
slSntpConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:slSntpConfigEntry.setStatus(_A)
_SlSntpConfigAddress_Type=IpAddress
_SlSntpConfigAddress_Object=MibTableColumn
slSntpConfigAddress=_SlSntpConfigAddress_Object((1,3,6,1,4,1,4515,1,3,21,1,10,1,1),_SlSntpConfigAddress_Type())
slSntpConfigAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:slSntpConfigAddress.setStatus(_A)
class _SlSntpConfigVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_SlSntpConfigVersion_Type.__name__=_B
_SlSntpConfigVersion_Object=MibTableColumn
slSntpConfigVersion=_SlSntpConfigVersion_Object((1,3,6,1,4,1,4515,1,3,21,1,10,1,2),_SlSntpConfigVersion_Type())
slSntpConfigVersion.setMaxAccess(_F)
if mibBuilder.loadTexts:slSntpConfigVersion.setStatus(_A)
class _SlSntpConfigPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SlSntpConfigPriority_Type.__name__=_B
_SlSntpConfigPriority_Object=MibTableColumn
slSntpConfigPriority=_SlSntpConfigPriority_Object((1,3,6,1,4,1,4515,1,3,21,1,10,1,3),_SlSntpConfigPriority_Type())
slSntpConfigPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:slSntpConfigPriority.setStatus(_A)
_SlSntpConfigRowStatus_Type=RowStatus
_SlSntpConfigRowStatus_Object=MibTableColumn
slSntpConfigRowStatus=_SlSntpConfigRowStatus_Object((1,3,6,1,4,1,4515,1,3,21,1,10,1,4),_SlSntpConfigRowStatus_Type())
slSntpConfigRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:slSntpConfigRowStatus.setStatus(_A)
class _SlSntpConfigMaxVariance_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7200000))
_SlSntpConfigMaxVariance_Type.__name__=_B
_SlSntpConfigMaxVariance_Object=MibTableColumn
slSntpConfigMaxVariance=_SlSntpConfigMaxVariance_Object((1,3,6,1,4,1,4515,1,3,21,1,10,1,5),_SlSntpConfigMaxVariance_Type())
slSntpConfigMaxVariance.setMaxAccess(_C)
if mibBuilder.loadTexts:slSntpConfigMaxVariance.setStatus(_A)
_SlSntpConfigVariance_Type=Integer32
_SlSntpConfigVariance_Object=MibTableColumn
slSntpConfigVariance=_SlSntpConfigVariance_Object((1,3,6,1,4,1,4515,1,3,21,1,10,1,6),_SlSntpConfigVariance_Type())
slSntpConfigVariance.setMaxAccess(_H)
if mibBuilder.loadTexts:slSntpConfigVariance.setStatus(_A)
class _SlSntpConfigVarianceDetectEnable_Type(TruthValue):defaultValue=2
_SlSntpConfigVarianceDetectEnable_Type.__name__=_G
_SlSntpConfigVarianceDetectEnable_Object=MibTableColumn
slSntpConfigVarianceDetectEnable=_SlSntpConfigVarianceDetectEnable_Object((1,3,6,1,4,1,4515,1,3,21,1,10,1,7),_SlSntpConfigVarianceDetectEnable_Type())
slSntpConfigVarianceDetectEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:slSntpConfigVarianceDetectEnable.setStatus(_A)
class _SlSntpConfigServerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unknown',0),('disconnected',1),('connected',2)))
_SlSntpConfigServerStatus_Type.__name__=_B
_SlSntpConfigServerStatus_Object=MibTableColumn
slSntpConfigServerStatus=_SlSntpConfigServerStatus_Object((1,3,6,1,4,1,4515,1,3,21,1,10,1,8),_SlSntpConfigServerStatus_Type())
slSntpConfigServerStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:slSntpConfigServerStatus.setStatus(_A)
_SlSntpTraps_ObjectIdentity=ObjectIdentity
slSntpTraps=_SlSntpTraps_ObjectIdentity((1,3,6,1,4,1,4515,1,3,21,2))
slSntpPeerFailureTrap=NotificationType((1,3,6,1,4,1,4515,1,3,21,2,1))
slSntpPeerFailureTrap.setObjects((_D,_E))
if mibBuilder.loadTexts:slSntpPeerFailureTrap.setStatus(_A)
slSntpConfigVarianceTrap=NotificationType((1,3,6,1,4,1,4515,1,3,21,2,2))
slSntpConfigVarianceTrap.setObjects(*((_D,_E),(_D,_I),(_D,_J)))
if mibBuilder.loadTexts:slSntpConfigVarianceTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'slSntp':slSntp,'slSntpConfig':slSntpConfig,'slSntpConfigMode':slSntpConfigMode,'slSntpConfigPollInterval':slSntpConfigPollInterval,'slSntpConfigRetryCount':slSntpConfigRetryCount,'slSntpConfigTimeZone':slSntpConfigTimeZone,'slSntpConfigDayLightSaving':slSntpConfigDayLightSaving,'slSntpConfigFractTimeZone':slSntpConfigFractTimeZone,'slSntpConfigTable':slSntpConfigTable,'slSntpConfigEntry':slSntpConfigEntry,_E:slSntpConfigAddress,'slSntpConfigVersion':slSntpConfigVersion,'slSntpConfigPriority':slSntpConfigPriority,'slSntpConfigRowStatus':slSntpConfigRowStatus,_I:slSntpConfigMaxVariance,_J:slSntpConfigVariance,'slSntpConfigVarianceDetectEnable':slSntpConfigVarianceDetectEnable,'slSntpConfigServerStatus':slSntpConfigServerStatus,'slSntpTraps':slSntpTraps,'slSntpPeerFailureTrap':slSntpPeerFailureTrap,'slSntpConfigVarianceTrap':slSntpConfigVarianceTrap})