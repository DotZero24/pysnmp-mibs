_Q='mwiConfigVer1'
_P='mwiIfConfigVer1'
_O='mwiExpirationTime'
_N='mwiFetchDigitMap'
_M='mwiConfigFetchAddress'
_L='mwiConfigUserSubscriptionAddress'
_K='mwiConfigActivation'
_J='Unsigned32'
_I='Integer32'
_H='MxDigitMap'
_G='ifIndex'
_F='IF-MIB'
_E='MxSignalingAddress'
_D='MxEnableState'
_C='read-write'
_B='MX-MESSAGE-WAITING-INDICATOR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
mediatrixConfig,=mibBuilder.importSymbols('MX-SMI','mediatrixConfig')
MxDigitMap,MxEnableState,MxSignalingAddress=mibBuilder.importSymbols('MX-TC',_H,_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
messageWaitingIndicatorMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,100))
if mibBuilder.loadTexts:messageWaitingIndicatorMIB.setRevisions(('2010-08-04 00:00','1903-08-29 00:00'))
_MwiMIBObjects_ObjectIdentity=ObjectIdentity
mwiMIBObjects=_MwiMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,100,1))
class _MwiFetchDigitMap_Type(MxDigitMap):defaultValue=OctetString('')
_MwiFetchDigitMap_Type.__name__=_H
_MwiFetchDigitMap_Object=MibScalar
mwiFetchDigitMap=_MwiFetchDigitMap_Object((1,3,6,1,4,1,4935,15,100,1,10),_MwiFetchDigitMap_Type())
mwiFetchDigitMap.setMaxAccess(_C)
if mibBuilder.loadTexts:mwiFetchDigitMap.setStatus(_A)
class _MwiExpirationTime_Type(Unsigned32):defaultValue=3600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(180,604800))
_MwiExpirationTime_Type.__name__=_J
_MwiExpirationTime_Object=MibScalar
mwiExpirationTime=_MwiExpirationTime_Object((1,3,6,1,4,1,4935,15,100,1,20),_MwiExpirationTime_Type())
mwiExpirationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mwiExpirationTime.setStatus(_A)
class _MwiSubscriptionCmdRefresh_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noOp',0),('refresh',1)))
_MwiSubscriptionCmdRefresh_Type.__name__=_I
_MwiSubscriptionCmdRefresh_Object=MibScalar
mwiSubscriptionCmdRefresh=_MwiSubscriptionCmdRefresh_Object((1,3,6,1,4,1,4935,15,100,1,30),_MwiSubscriptionCmdRefresh_Type())
mwiSubscriptionCmdRefresh.setMaxAccess(_C)
if mibBuilder.loadTexts:mwiSubscriptionCmdRefresh.setStatus(_A)
_MwiIfConfigurationTable_Object=MibTable
mwiIfConfigurationTable=_MwiIfConfigurationTable_Object((1,3,6,1,4,1,4935,15,100,1,40))
if mibBuilder.loadTexts:mwiIfConfigurationTable.setStatus(_A)
_MwiIfConfigurationEntry_Object=MibTableRow
mwiIfConfigurationEntry=_MwiIfConfigurationEntry_Object((1,3,6,1,4,1,4935,15,100,1,40,1))
mwiIfConfigurationEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:mwiIfConfigurationEntry.setStatus(_A)
class _MwiConfigActivation_Type(MxEnableState):defaultValue=0
_MwiConfigActivation_Type.__name__=_D
_MwiConfigActivation_Object=MibTableColumn
mwiConfigActivation=_MwiConfigActivation_Object((1,3,6,1,4,1,4935,15,100,1,40,1,5),_MwiConfigActivation_Type())
mwiConfigActivation.setMaxAccess(_C)
if mibBuilder.loadTexts:mwiConfigActivation.setStatus(_A)
class _MwiConfigUserSubscriptionAddress_Type(MxSignalingAddress):defaultValue=OctetString('')
_MwiConfigUserSubscriptionAddress_Type.__name__=_E
_MwiConfigUserSubscriptionAddress_Object=MibTableColumn
mwiConfigUserSubscriptionAddress=_MwiConfigUserSubscriptionAddress_Object((1,3,6,1,4,1,4935,15,100,1,40,1,10),_MwiConfigUserSubscriptionAddress_Type())
mwiConfigUserSubscriptionAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mwiConfigUserSubscriptionAddress.setStatus(_A)
class _MwiConfigFetchAddress_Type(MxSignalingAddress):defaultValue=OctetString('')
_MwiConfigFetchAddress_Type.__name__=_E
_MwiConfigFetchAddress_Object=MibTableColumn
mwiConfigFetchAddress=_MwiConfigFetchAddress_Object((1,3,6,1,4,1,4935,15,100,1,40,1,15),_MwiConfigFetchAddress_Type())
mwiConfigFetchAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mwiConfigFetchAddress.setStatus(_A)
class _MwiConfigVoltageEnable_Type(MxEnableState):defaultValue=0
_MwiConfigVoltageEnable_Type.__name__=_D
_MwiConfigVoltageEnable_Object=MibScalar
mwiConfigVoltageEnable=_MwiConfigVoltageEnable_Object((1,3,6,1,4,1,4935,15,100,1,40,1,20),_MwiConfigVoltageEnable_Type())
mwiConfigVoltageEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:mwiConfigVoltageEnable.setStatus(_A)
_MwiConformance_ObjectIdentity=ObjectIdentity
mwiConformance=_MwiConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,100,10))
_MwiCompliances_ObjectIdentity=ObjectIdentity
mwiCompliances=_MwiCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,100,10,1))
_MwiGroups_ObjectIdentity=ObjectIdentity
mwiGroups=_MwiGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,100,10,5))
mwiIfConfigVer1=ObjectGroup((1,3,6,1,4,1,4935,15,100,10,5,3))
mwiIfConfigVer1.setObjects(*((_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:mwiIfConfigVer1.setStatus(_A)
mwiConfigVer1=ObjectGroup((1,3,6,1,4,1,4935,15,100,10,5,6))
mwiConfigVer1.setObjects(*((_B,_N),(_B,_O)))
if mibBuilder.loadTexts:mwiConfigVer1.setStatus(_A)
mwiComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,100,10,1,1))
mwiComplVer1.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:mwiComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'messageWaitingIndicatorMIB':messageWaitingIndicatorMIB,'mwiMIBObjects':mwiMIBObjects,_N:mwiFetchDigitMap,_O:mwiExpirationTime,'mwiSubscriptionCmdRefresh':mwiSubscriptionCmdRefresh,'mwiIfConfigurationTable':mwiIfConfigurationTable,'mwiIfConfigurationEntry':mwiIfConfigurationEntry,_K:mwiConfigActivation,_L:mwiConfigUserSubscriptionAddress,_M:mwiConfigFetchAddress,'mwiConfigVoltageEnable':mwiConfigVoltageEnable,'mwiConformance':mwiConformance,'mwiCompliances':mwiCompliances,'mwiComplVer1':mwiComplVer1,'mwiGroups':mwiGroups,_P:mwiIfConfigVer1,_Q:mwiConfigVer1})