_M='ipRoutesStatusIndex'
_L='advancedIpRoutesStatusId'
_K='staticIpRoutesIndex'
_J='delete'
_I='advancedIpRoutesId'
_H='Unsigned32'
_G='MxEnableState'
_F='MX-IPROUTING-MIB'
_E='OctetString'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap',_G,'MxIpAddress','MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort','MxIpHostNamePort','MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ipRoutingMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,3500))
_IpRoutingMIBObjects_ObjectIdentity=ObjectIdentity
ipRoutingMIBObjects=_IpRoutingMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,3500,1))
_AdvancedIpRoutesTable_Object=MibTable
advancedIpRoutesTable=_AdvancedIpRoutesTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,200))
if mibBuilder.loadTexts:advancedIpRoutesTable.setStatus(_A)
_AdvancedIpRoutesEntry_Object=MibTableRow
advancedIpRoutesEntry=_AdvancedIpRoutesEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,200,1))
advancedIpRoutesEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:advancedIpRoutesEntry.setStatus(_A)
_AdvancedIpRoutesId_Type=Unsigned32
_AdvancedIpRoutesId_Object=MibTableColumn
advancedIpRoutesId=_AdvancedIpRoutesId_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,200,1,50),_AdvancedIpRoutesId_Type())
advancedIpRoutesId.setMaxAccess(_B)
if mibBuilder.loadTexts:advancedIpRoutesId.setStatus(_A)
class _AdvancedIpRoutesPriority_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,252))
_AdvancedIpRoutesPriority_Type.__name__=_H
_AdvancedIpRoutesPriority_Object=MibTableColumn
advancedIpRoutesPriority=_AdvancedIpRoutesPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,200,1,100),_AdvancedIpRoutesPriority_Type())
advancedIpRoutesPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:advancedIpRoutesPriority.setStatus(_A)
class _AdvancedIpRoutesActivation_Type(MxEnableState):defaultValue=0
_AdvancedIpRoutesActivation_Type.__name__=_G
_AdvancedIpRoutesActivation_Object=MibTableColumn
advancedIpRoutesActivation=_AdvancedIpRoutesActivation_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,200,1,200),_AdvancedIpRoutesActivation_Type())
advancedIpRoutesActivation.setMaxAccess(_C)
if mibBuilder.loadTexts:advancedIpRoutesActivation.setStatus(_A)
class _AdvancedIpRoutesSourceAddress_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,51))
_AdvancedIpRoutesSourceAddress_Type.__name__=_E
_AdvancedIpRoutesSourceAddress_Object=MibTableColumn
advancedIpRoutesSourceAddress=_AdvancedIpRoutesSourceAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,200,1,300),_AdvancedIpRoutesSourceAddress_Type())
advancedIpRoutesSourceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:advancedIpRoutesSourceAddress.setStatus(_A)
class _AdvancedIpRoutesSourceLink_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,51))
_AdvancedIpRoutesSourceLink_Type.__name__=_E
_AdvancedIpRoutesSourceLink_Object=MibTableColumn
advancedIpRoutesSourceLink=_AdvancedIpRoutesSourceLink_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,200,1,400),_AdvancedIpRoutesSourceLink_Type())
advancedIpRoutesSourceLink.setMaxAccess(_C)
if mibBuilder.loadTexts:advancedIpRoutesSourceLink.setStatus(_A)
class _AdvancedIpRoutesForwardToNetwork_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,51))
_AdvancedIpRoutesForwardToNetwork_Type.__name__=_E
_AdvancedIpRoutesForwardToNetwork_Object=MibTableColumn
advancedIpRoutesForwardToNetwork=_AdvancedIpRoutesForwardToNetwork_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,200,1,500),_AdvancedIpRoutesForwardToNetwork_Type())
advancedIpRoutesForwardToNetwork.setMaxAccess(_C)
if mibBuilder.loadTexts:advancedIpRoutesForwardToNetwork.setStatus(_A)
class _AdvancedIpRoutesDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*(('noOp',0),(_J,10)))
_AdvancedIpRoutesDelete_Type.__name__=_D
_AdvancedIpRoutesDelete_Object=MibTableColumn
advancedIpRoutesDelete=_AdvancedIpRoutesDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,200,1,900),_AdvancedIpRoutesDelete_Type())
advancedIpRoutesDelete.setMaxAccess(_C)
if mibBuilder.loadTexts:advancedIpRoutesDelete.setStatus(_A)
_StaticIpRoutesTable_Object=MibTable
staticIpRoutesTable=_StaticIpRoutesTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,600))
if mibBuilder.loadTexts:staticIpRoutesTable.setStatus(_A)
_StaticIpRoutesEntry_Object=MibTableRow
staticIpRoutesEntry=_StaticIpRoutesEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,600,1))
staticIpRoutesEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:staticIpRoutesEntry.setStatus(_A)
_StaticIpRoutesIndex_Type=Unsigned32
_StaticIpRoutesIndex_Object=MibTableColumn
staticIpRoutesIndex=_StaticIpRoutesIndex_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,600,1,100),_StaticIpRoutesIndex_Type())
staticIpRoutesIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:staticIpRoutesIndex.setStatus(_A)
class _StaticIpRoutesLink_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,51))
_StaticIpRoutesLink_Type.__name__=_E
_StaticIpRoutesLink_Object=MibTableColumn
staticIpRoutesLink=_StaticIpRoutesLink_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,600,1,200),_StaticIpRoutesLink_Type())
staticIpRoutesLink.setMaxAccess(_C)
if mibBuilder.loadTexts:staticIpRoutesLink.setStatus(_A)
class _StaticIpRoutesDestination_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,51))
_StaticIpRoutesDestination_Type.__name__=_E
_StaticIpRoutesDestination_Object=MibTableColumn
staticIpRoutesDestination=_StaticIpRoutesDestination_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,600,1,300),_StaticIpRoutesDestination_Type())
staticIpRoutesDestination.setMaxAccess(_C)
if mibBuilder.loadTexts:staticIpRoutesDestination.setStatus(_A)
class _StaticIpRoutesGateway_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,51))
_StaticIpRoutesGateway_Type.__name__=_E
_StaticIpRoutesGateway_Object=MibTableColumn
staticIpRoutesGateway=_StaticIpRoutesGateway_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,600,1,400),_StaticIpRoutesGateway_Type())
staticIpRoutesGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:staticIpRoutesGateway.setStatus(_A)
class _StaticIpRoutesDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*(('noOp',0),(_J,10)))
_StaticIpRoutesDelete_Type.__name__=_D
_StaticIpRoutesDelete_Object=MibTableColumn
staticIpRoutesDelete=_StaticIpRoutesDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,600,1,500),_StaticIpRoutesDelete_Type())
staticIpRoutesDelete.setMaxAccess(_C)
if mibBuilder.loadTexts:staticIpRoutesDelete.setStatus(_A)
class _Ipv4ForwardingEnable_Type(MxEnableState):defaultValue=1
_Ipv4ForwardingEnable_Type.__name__=_G
_Ipv4ForwardingEnable_Object=MibScalar
ipv4ForwardingEnable=_Ipv4ForwardingEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,800),_Ipv4ForwardingEnable_Type())
ipv4ForwardingEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ipv4ForwardingEnable.setStatus(_A)
_StatusGroup_ObjectIdentity=ObjectIdentity
statusGroup=_StatusGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,10000))
class _ConfigModifiedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('yes',100),('no',200)))
_ConfigModifiedStatus_Type.__name__=_D
_ConfigModifiedStatus_Object=MibScalar
configModifiedStatus=_ConfigModifiedStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,10000,100),_ConfigModifiedStatus_Type())
configModifiedStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:configModifiedStatus.setStatus(_A)
_AdvancedIpRoutesStatusTable_Object=MibTable
advancedIpRoutesStatusTable=_AdvancedIpRoutesStatusTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,10000,200))
if mibBuilder.loadTexts:advancedIpRoutesStatusTable.setStatus(_A)
_AdvancedIpRoutesStatusEntry_Object=MibTableRow
advancedIpRoutesStatusEntry=_AdvancedIpRoutesStatusEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,10000,200,1))
advancedIpRoutesStatusEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:advancedIpRoutesStatusEntry.setStatus(_A)
_AdvancedIpRoutesStatusId_Type=Unsigned32
_AdvancedIpRoutesStatusId_Object=MibTableColumn
advancedIpRoutesStatusId=_AdvancedIpRoutesStatusId_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,10000,200,1,50),_AdvancedIpRoutesStatusId_Type())
advancedIpRoutesStatusId.setMaxAccess(_B)
if mibBuilder.loadTexts:advancedIpRoutesStatusId.setStatus(_A)
_AdvancedIpRoutesStatusPriority_Type=Unsigned32
_AdvancedIpRoutesStatusPriority_Object=MibTableColumn
advancedIpRoutesStatusPriority=_AdvancedIpRoutesStatusPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,10000,200,1,100),_AdvancedIpRoutesStatusPriority_Type())
advancedIpRoutesStatusPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:advancedIpRoutesStatusPriority.setStatus(_A)
_AdvancedIpRoutesStatusSourceAddress_Type=OctetString
_AdvancedIpRoutesStatusSourceAddress_Object=MibTableColumn
advancedIpRoutesStatusSourceAddress=_AdvancedIpRoutesStatusSourceAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,10000,200,1,200),_AdvancedIpRoutesStatusSourceAddress_Type())
advancedIpRoutesStatusSourceAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:advancedIpRoutesStatusSourceAddress.setStatus(_A)
_AdvancedIpRoutesStatusSourceLink_Type=OctetString
_AdvancedIpRoutesStatusSourceLink_Object=MibTableColumn
advancedIpRoutesStatusSourceLink=_AdvancedIpRoutesStatusSourceLink_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,10000,200,1,300),_AdvancedIpRoutesStatusSourceLink_Type())
advancedIpRoutesStatusSourceLink.setMaxAccess(_B)
if mibBuilder.loadTexts:advancedIpRoutesStatusSourceLink.setStatus(_A)
_AdvancedIpRoutesStatusForwardToNetwork_Type=OctetString
_AdvancedIpRoutesStatusForwardToNetwork_Object=MibTableColumn
advancedIpRoutesStatusForwardToNetwork=_AdvancedIpRoutesStatusForwardToNetwork_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,10000,200,1,350),_AdvancedIpRoutesStatusForwardToNetwork_Type())
advancedIpRoutesStatusForwardToNetwork.setMaxAccess(_B)
if mibBuilder.loadTexts:advancedIpRoutesStatusForwardToNetwork.setStatus(_A)
class _AdvancedIpRoutesStatusStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('disabled',100),('invalidConfig',200),('active',300),('duplicatePriority',400)))
_AdvancedIpRoutesStatusStatus_Type.__name__=_D
_AdvancedIpRoutesStatusStatus_Object=MibTableColumn
advancedIpRoutesStatusStatus=_AdvancedIpRoutesStatusStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,10000,200,1,400),_AdvancedIpRoutesStatusStatus_Type())
advancedIpRoutesStatusStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:advancedIpRoutesStatusStatus.setStatus(_A)
_IpRoutesStatusTable_Object=MibTable
ipRoutesStatusTable=_IpRoutesStatusTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,10000,300))
if mibBuilder.loadTexts:ipRoutesStatusTable.setStatus(_A)
_IpRoutesStatusEntry_Object=MibTableRow
ipRoutesStatusEntry=_IpRoutesStatusEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,10000,300,1))
ipRoutesStatusEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:ipRoutesStatusEntry.setStatus(_A)
_IpRoutesStatusIndex_Type=Unsigned32
_IpRoutesStatusIndex_Object=MibTableColumn
ipRoutesStatusIndex=_IpRoutesStatusIndex_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,10000,300,1,100),_IpRoutesStatusIndex_Type())
ipRoutesStatusIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRoutesStatusIndex.setStatus(_A)
_IpRoutesStatusLink_Type=OctetString
_IpRoutesStatusLink_Object=MibTableColumn
ipRoutesStatusLink=_IpRoutesStatusLink_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,10000,300,1,200),_IpRoutesStatusLink_Type())
ipRoutesStatusLink.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRoutesStatusLink.setStatus(_A)
_IpRoutesStatusDestination_Type=OctetString
_IpRoutesStatusDestination_Object=MibTableColumn
ipRoutesStatusDestination=_IpRoutesStatusDestination_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,10000,300,1,300),_IpRoutesStatusDestination_Type())
ipRoutesStatusDestination.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRoutesStatusDestination.setStatus(_A)
_IpRoutesStatusGateway_Type=OctetString
_IpRoutesStatusGateway_Object=MibTableColumn
ipRoutesStatusGateway=_IpRoutesStatusGateway_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,10000,300,1,400),_IpRoutesStatusGateway_Type())
ipRoutesStatusGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRoutesStatusGateway.setStatus(_A)
class _IpRoutesStatusProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('other',100),('kernel',200),('static',300),('dhcp',400)))
_IpRoutesStatusProtocol_Type.__name__=_D
_IpRoutesStatusProtocol_Object=MibTableColumn
ipRoutesStatusProtocol=_IpRoutesStatusProtocol_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,10000,300,1,500),_IpRoutesStatusProtocol_Type())
ipRoutesStatusProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:ipRoutesStatusProtocol.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_D
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_D
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,3500,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'ipRoutingMIB':ipRoutingMIB,'ipRoutingMIBObjects':ipRoutingMIBObjects,'advancedIpRoutesTable':advancedIpRoutesTable,'advancedIpRoutesEntry':advancedIpRoutesEntry,_I:advancedIpRoutesId,'advancedIpRoutesPriority':advancedIpRoutesPriority,'advancedIpRoutesActivation':advancedIpRoutesActivation,'advancedIpRoutesSourceAddress':advancedIpRoutesSourceAddress,'advancedIpRoutesSourceLink':advancedIpRoutesSourceLink,'advancedIpRoutesForwardToNetwork':advancedIpRoutesForwardToNetwork,'advancedIpRoutesDelete':advancedIpRoutesDelete,'staticIpRoutesTable':staticIpRoutesTable,'staticIpRoutesEntry':staticIpRoutesEntry,_K:staticIpRoutesIndex,'staticIpRoutesLink':staticIpRoutesLink,'staticIpRoutesDestination':staticIpRoutesDestination,'staticIpRoutesGateway':staticIpRoutesGateway,'staticIpRoutesDelete':staticIpRoutesDelete,'ipv4ForwardingEnable':ipv4ForwardingEnable,'statusGroup':statusGroup,'configModifiedStatus':configModifiedStatus,'advancedIpRoutesStatusTable':advancedIpRoutesStatusTable,'advancedIpRoutesStatusEntry':advancedIpRoutesStatusEntry,_L:advancedIpRoutesStatusId,'advancedIpRoutesStatusPriority':advancedIpRoutesStatusPriority,'advancedIpRoutesStatusSourceAddress':advancedIpRoutesStatusSourceAddress,'advancedIpRoutesStatusSourceLink':advancedIpRoutesStatusSourceLink,'advancedIpRoutesStatusForwardToNetwork':advancedIpRoutesStatusForwardToNetwork,'advancedIpRoutesStatusStatus':advancedIpRoutesStatusStatus,'ipRoutesStatusTable':ipRoutesStatusTable,'ipRoutesStatusEntry':ipRoutesStatusEntry,_M:ipRoutesStatusIndex,'ipRoutesStatusLink':ipRoutesStatusLink,'ipRoutesStatusDestination':ipRoutesStatusDestination,'ipRoutesStatusGateway':ipRoutesStatusGateway,'ipRoutesStatusProtocol':ipRoutesStatusProtocol,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})