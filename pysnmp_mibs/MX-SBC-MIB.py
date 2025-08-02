_s='callAgentStatsCallAgent'
_r='registrationAgentStatusId'
_q='routingRulesStatusId'
_p='callAgentRulesetStatusId'
_o='mediaInterfaceStatusId'
_n='noIpAddress'
_m='signalingInterfaceStatusId'
_l='callAgentStatusId'
_k='staticRegistrationRegistrationId'
_j='prefixBasedRoutingRuleId'
_i='peerMonitoringId'
_h='registrationAgentId'
_g='mediaInterfaceId'
_f='portConflict'
_e='unknownNetworkInterface'
_d='tlsOnly'
_c='server'
_b='client'
_a='signalingInterfaceId'
_Z='routingRulesetCatalogId'
_Y='routingRulesId'
_X='custom'
_W='factory'
_V='callAgentRulesetCatalogId'
_U='unknownRuleset'
_T='callAgentRulesetId'
_S='callAgentId'
_R='MxIpHostNamePort'
_Q='MxIpAddrMask'
_P='MxEnableState'
_O='networkDown'
_N='active'
_M='none'
_L='MxIpAddress'
_K='delete'
_J='noOp'
_I='invalidConfig'
_H='valid'
_G='MX-SBC-MIB'
_F='Unsigned32'
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
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap',_P,_L,'MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr',_Q,'MxIpAddrPort',_R,'MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sbcMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4400))
_SbcMIBObjects_ObjectIdentity=ObjectIdentity
sbcMIBObjects=_SbcMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4400,1))
_ConfigGroup_ObjectIdentity=ObjectIdentity
configGroup=_ConfigGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100))
_CallAgentTable_Object=MibTable
callAgentTable=_CallAgentTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,100))
if mibBuilder.loadTexts:callAgentTable.setStatus(_A)
_CallAgentEntry_Object=MibTableRow
callAgentEntry=_CallAgentEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,100,1))
callAgentEntry.setIndexNames((0,_G,_S))
if mibBuilder.loadTexts:callAgentEntry.setStatus(_A)
class _CallAgentId_Type(Unsigned32):defaultValue=0
_CallAgentId_Type.__name__=_F
_CallAgentId_Object=MibTableColumn
callAgentId=_CallAgentId_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,100,1,100),_CallAgentId_Type())
callAgentId.setMaxAccess(_B)
if mibBuilder.loadTexts:callAgentId.setStatus(_A)
class _CallAgentName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_CallAgentName_Type.__name__=_E
_CallAgentName_Object=MibTableColumn
callAgentName=_CallAgentName_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,100,1,200),_CallAgentName_Type())
callAgentName.setMaxAccess(_C)
if mibBuilder.loadTexts:callAgentName.setStatus(_A)
class _CallAgentEnable_Type(MxEnableState):defaultValue=0
_CallAgentEnable_Type.__name__=_P
_CallAgentEnable_Object=MibTableColumn
callAgentEnable=_CallAgentEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,100,1,300),_CallAgentEnable_Type())
callAgentEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:callAgentEnable.setStatus(_A)
class _CallAgentSignalingInterface_Type(Unsigned32):defaultValue=0
_CallAgentSignalingInterface_Type.__name__=_F
_CallAgentSignalingInterface_Object=MibTableColumn
callAgentSignalingInterface=_CallAgentSignalingInterface_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,100,1,400),_CallAgentSignalingInterface_Type())
callAgentSignalingInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:callAgentSignalingInterface.setStatus(_A)
class _CallAgentMediaInterface_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_CallAgentMediaInterface_Type.__name__=_E
_CallAgentMediaInterface_Object=MibTableColumn
callAgentMediaInterface=_CallAgentMediaInterface_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,100,1,500),_CallAgentMediaInterface_Type())
callAgentMediaInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:callAgentMediaInterface.setStatus(_A)
class _CallAgentGateway_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_CallAgentGateway_Type.__name__=_E
_CallAgentGateway_Object=MibTableColumn
callAgentGateway=_CallAgentGateway_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,100,1,600),_CallAgentGateway_Type())
callAgentGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:callAgentGateway.setStatus(_A)
class _CallAgentPeerHost_Type(MxIpHostNamePort):defaultValue=OctetString('')
_CallAgentPeerHost_Type.__name__=_R
_CallAgentPeerHost_Object=MibTableColumn
callAgentPeerHost=_CallAgentPeerHost_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,100,1,700),_CallAgentPeerHost_Type())
callAgentPeerHost.setMaxAccess(_C)
if mibBuilder.loadTexts:callAgentPeerHost.setStatus(_A)
class _CallAgentPeerNetwork_Type(MxIpAddrMask):defaultValue=OctetString('')
_CallAgentPeerNetwork_Type.__name__=_Q
_CallAgentPeerNetwork_Object=MibTableColumn
callAgentPeerNetwork=_CallAgentPeerNetwork_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,100,1,800),_CallAgentPeerNetwork_Type())
callAgentPeerNetwork.setMaxAccess(_C)
if mibBuilder.loadTexts:callAgentPeerNetwork.setStatus(_A)
class _CallAgentForceTransport_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*((_M,100),('tCP',200),('uDP',300),('tLS',400)))
_CallAgentForceTransport_Type.__name__=_D
_CallAgentForceTransport_Object=MibTableColumn
callAgentForceTransport=_CallAgentForceTransport_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,100,1,900),_CallAgentForceTransport_Type())
callAgentForceTransport.setMaxAccess(_C)
if mibBuilder.loadTexts:callAgentForceTransport.setStatus(_A)
class _CallAgentConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600)));namedValues=NamedValues(*((_H,100),('unknownSignalingInterface',200),('unknownMediaInterface',300),('invalidGatewayBinding',400),(_I,500),('noMediaInterface',600)))
_CallAgentConfigStatus_Type.__name__=_D
_CallAgentConfigStatus_Object=MibTableColumn
callAgentConfigStatus=_CallAgentConfigStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,100,1,1000),_CallAgentConfigStatus_Type())
callAgentConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:callAgentConfigStatus.setStatus(_A)
class _CallAgentDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_J,0),(_K,10)))
_CallAgentDelete_Type.__name__=_D
_CallAgentDelete_Object=MibTableColumn
callAgentDelete=_CallAgentDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,100,1,10000),_CallAgentDelete_Type())
callAgentDelete.setMaxAccess(_C)
if mibBuilder.loadTexts:callAgentDelete.setStatus(_A)
_CallAgentRulesetTable_Object=MibTable
callAgentRulesetTable=_CallAgentRulesetTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,200))
if mibBuilder.loadTexts:callAgentRulesetTable.setStatus(_A)
_CallAgentRulesetEntry_Object=MibTableRow
callAgentRulesetEntry=_CallAgentRulesetEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,200,1))
callAgentRulesetEntry.setIndexNames((0,_G,_T))
if mibBuilder.loadTexts:callAgentRulesetEntry.setStatus(_A)
class _CallAgentRulesetId_Type(Unsigned32):defaultValue=0
_CallAgentRulesetId_Type.__name__=_F
_CallAgentRulesetId_Object=MibTableColumn
callAgentRulesetId=_CallAgentRulesetId_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,200,1,100),_CallAgentRulesetId_Type())
callAgentRulesetId.setMaxAccess(_B)
if mibBuilder.loadTexts:callAgentRulesetId.setStatus(_A)
class _CallAgentRulesetCallAgent_Type(Unsigned32):defaultValue=0
_CallAgentRulesetCallAgent_Type.__name__=_F
_CallAgentRulesetCallAgent_Object=MibTableColumn
callAgentRulesetCallAgent=_CallAgentRulesetCallAgent_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,200,1,200),_CallAgentRulesetCallAgent_Type())
callAgentRulesetCallAgent.setMaxAccess(_C)
if mibBuilder.loadTexts:callAgentRulesetCallAgent.setStatus(_A)
class _CallAgentRulesetPriority_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CallAgentRulesetPriority_Type.__name__=_F
_CallAgentRulesetPriority_Object=MibTableColumn
callAgentRulesetPriority=_CallAgentRulesetPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,200,1,300),_CallAgentRulesetPriority_Type())
callAgentRulesetPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:callAgentRulesetPriority.setStatus(_A)
class _CallAgentRulesetRuleset_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_CallAgentRulesetRuleset_Type.__name__=_E
_CallAgentRulesetRuleset_Object=MibTableColumn
callAgentRulesetRuleset=_CallAgentRulesetRuleset_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,200,1,400),_CallAgentRulesetRuleset_Type())
callAgentRulesetRuleset.setMaxAccess(_C)
if mibBuilder.loadTexts:callAgentRulesetRuleset.setStatus(_A)
class _CallAgentRulesetParameters_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_CallAgentRulesetParameters_Type.__name__=_E
_CallAgentRulesetParameters_Object=MibTableColumn
callAgentRulesetParameters=_CallAgentRulesetParameters_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,200,1,500),_CallAgentRulesetParameters_Type())
callAgentRulesetParameters.setMaxAccess(_C)
if mibBuilder.loadTexts:callAgentRulesetParameters.setStatus(_A)
class _CallAgentRulesetConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_H,100),(_U,200),(_I,300)))
_CallAgentRulesetConfigStatus_Type.__name__=_D
_CallAgentRulesetConfigStatus_Object=MibTableColumn
callAgentRulesetConfigStatus=_CallAgentRulesetConfigStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,200,1,600),_CallAgentRulesetConfigStatus_Type())
callAgentRulesetConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:callAgentRulesetConfigStatus.setStatus(_A)
class _CallAgentRulesetDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_J,0),(_K,10)))
_CallAgentRulesetDelete_Type.__name__=_D
_CallAgentRulesetDelete_Object=MibTableColumn
callAgentRulesetDelete=_CallAgentRulesetDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,200,1,10000),_CallAgentRulesetDelete_Type())
callAgentRulesetDelete.setMaxAccess(_C)
if mibBuilder.loadTexts:callAgentRulesetDelete.setStatus(_A)
_CallAgentRulesetCatalogTable_Object=MibTable
callAgentRulesetCatalogTable=_CallAgentRulesetCatalogTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,250))
if mibBuilder.loadTexts:callAgentRulesetCatalogTable.setStatus(_A)
_CallAgentRulesetCatalogEntry_Object=MibTableRow
callAgentRulesetCatalogEntry=_CallAgentRulesetCatalogEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,250,1))
callAgentRulesetCatalogEntry.setIndexNames((0,_G,_V))
if mibBuilder.loadTexts:callAgentRulesetCatalogEntry.setStatus(_A)
_CallAgentRulesetCatalogId_Type=Unsigned32
_CallAgentRulesetCatalogId_Object=MibTableColumn
callAgentRulesetCatalogId=_CallAgentRulesetCatalogId_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,250,1,100),_CallAgentRulesetCatalogId_Type())
callAgentRulesetCatalogId.setMaxAccess(_B)
if mibBuilder.loadTexts:callAgentRulesetCatalogId.setStatus(_A)
class _CallAgentRulesetCatalogName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_CallAgentRulesetCatalogName_Type.__name__=_E
_CallAgentRulesetCatalogName_Object=MibTableColumn
callAgentRulesetCatalogName=_CallAgentRulesetCatalogName_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,250,1,200),_CallAgentRulesetCatalogName_Type())
callAgentRulesetCatalogName.setMaxAccess(_B)
if mibBuilder.loadTexts:callAgentRulesetCatalogName.setStatus(_A)
class _CallAgentRulesetCatalogDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_CallAgentRulesetCatalogDescription_Type.__name__=_E
_CallAgentRulesetCatalogDescription_Object=MibTableColumn
callAgentRulesetCatalogDescription=_CallAgentRulesetCatalogDescription_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,250,1,300),_CallAgentRulesetCatalogDescription_Type())
callAgentRulesetCatalogDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:callAgentRulesetCatalogDescription.setStatus(_A)
class _CallAgentRulesetCatalogOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_W,100),(_X,200)))
_CallAgentRulesetCatalogOrigin_Type.__name__=_D
_CallAgentRulesetCatalogOrigin_Object=MibTableColumn
callAgentRulesetCatalogOrigin=_CallAgentRulesetCatalogOrigin_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,250,1,400),_CallAgentRulesetCatalogOrigin_Type())
callAgentRulesetCatalogOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:callAgentRulesetCatalogOrigin.setStatus(_A)
_RoutingRulesTable_Object=MibTable
routingRulesTable=_RoutingRulesTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,300))
if mibBuilder.loadTexts:routingRulesTable.setStatus(_A)
_RoutingRulesEntry_Object=MibTableRow
routingRulesEntry=_RoutingRulesEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,300,1))
routingRulesEntry.setIndexNames((0,_G,_Y))
if mibBuilder.loadTexts:routingRulesEntry.setStatus(_A)
class _RoutingRulesId_Type(Unsigned32):defaultValue=0
_RoutingRulesId_Type.__name__=_F
_RoutingRulesId_Object=MibTableColumn
routingRulesId=_RoutingRulesId_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,300,1,100),_RoutingRulesId_Type())
routingRulesId.setMaxAccess(_B)
if mibBuilder.loadTexts:routingRulesId.setStatus(_A)
class _RoutingRulesPriority_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RoutingRulesPriority_Type.__name__=_F
_RoutingRulesPriority_Object=MibTableColumn
routingRulesPriority=_RoutingRulesPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,300,1,200),_RoutingRulesPriority_Type())
routingRulesPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:routingRulesPriority.setStatus(_A)
class _RoutingRulesRuleset_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_RoutingRulesRuleset_Type.__name__=_E
_RoutingRulesRuleset_Object=MibTableColumn
routingRulesRuleset=_RoutingRulesRuleset_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,300,1,300),_RoutingRulesRuleset_Type())
routingRulesRuleset.setMaxAccess(_C)
if mibBuilder.loadTexts:routingRulesRuleset.setStatus(_A)
class _RoutingRulesParameters_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_RoutingRulesParameters_Type.__name__=_E
_RoutingRulesParameters_Object=MibTableColumn
routingRulesParameters=_RoutingRulesParameters_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,300,1,400),_RoutingRulesParameters_Type())
routingRulesParameters.setMaxAccess(_C)
if mibBuilder.loadTexts:routingRulesParameters.setStatus(_A)
class _RoutingRulesConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_H,100),(_U,200),(_I,300)))
_RoutingRulesConfigStatus_Type.__name__=_D
_RoutingRulesConfigStatus_Object=MibTableColumn
routingRulesConfigStatus=_RoutingRulesConfigStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,300,1,500),_RoutingRulesConfigStatus_Type())
routingRulesConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:routingRulesConfigStatus.setStatus(_A)
class _RoutingRulesDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_J,0),(_K,10)))
_RoutingRulesDelete_Type.__name__=_D
_RoutingRulesDelete_Object=MibTableColumn
routingRulesDelete=_RoutingRulesDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,300,1,10000),_RoutingRulesDelete_Type())
routingRulesDelete.setMaxAccess(_C)
if mibBuilder.loadTexts:routingRulesDelete.setStatus(_A)
_RoutingRulesetCatalogTable_Object=MibTable
routingRulesetCatalogTable=_RoutingRulesetCatalogTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,350))
if mibBuilder.loadTexts:routingRulesetCatalogTable.setStatus(_A)
_RoutingRulesetCatalogEntry_Object=MibTableRow
routingRulesetCatalogEntry=_RoutingRulesetCatalogEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,350,1))
routingRulesetCatalogEntry.setIndexNames((0,_G,_Z))
if mibBuilder.loadTexts:routingRulesetCatalogEntry.setStatus(_A)
_RoutingRulesetCatalogId_Type=Unsigned32
_RoutingRulesetCatalogId_Object=MibTableColumn
routingRulesetCatalogId=_RoutingRulesetCatalogId_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,350,1,100),_RoutingRulesetCatalogId_Type())
routingRulesetCatalogId.setMaxAccess(_B)
if mibBuilder.loadTexts:routingRulesetCatalogId.setStatus(_A)
class _RoutingRulesetCatalogName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_RoutingRulesetCatalogName_Type.__name__=_E
_RoutingRulesetCatalogName_Object=MibTableColumn
routingRulesetCatalogName=_RoutingRulesetCatalogName_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,350,1,200),_RoutingRulesetCatalogName_Type())
routingRulesetCatalogName.setMaxAccess(_B)
if mibBuilder.loadTexts:routingRulesetCatalogName.setStatus(_A)
class _RoutingRulesetCatalogDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_RoutingRulesetCatalogDescription_Type.__name__=_E
_RoutingRulesetCatalogDescription_Object=MibTableColumn
routingRulesetCatalogDescription=_RoutingRulesetCatalogDescription_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,350,1,300),_RoutingRulesetCatalogDescription_Type())
routingRulesetCatalogDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:routingRulesetCatalogDescription.setStatus(_A)
class _RoutingRulesetCatalogOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_W,100),(_X,200)))
_RoutingRulesetCatalogOrigin_Type.__name__=_D
_RoutingRulesetCatalogOrigin_Object=MibTableColumn
routingRulesetCatalogOrigin=_RoutingRulesetCatalogOrigin_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,350,1,400),_RoutingRulesetCatalogOrigin_Type())
routingRulesetCatalogOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:routingRulesetCatalogOrigin.setStatus(_A)
_SignalingInterfaceTable_Object=MibTable
signalingInterfaceTable=_SignalingInterfaceTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,400))
if mibBuilder.loadTexts:signalingInterfaceTable.setStatus(_A)
_SignalingInterfaceEntry_Object=MibTableRow
signalingInterfaceEntry=_SignalingInterfaceEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,400,1))
signalingInterfaceEntry.setIndexNames((0,_G,_a))
if mibBuilder.loadTexts:signalingInterfaceEntry.setStatus(_A)
class _SignalingInterfaceId_Type(Unsigned32):defaultValue=0
_SignalingInterfaceId_Type.__name__=_F
_SignalingInterfaceId_Object=MibTableColumn
signalingInterfaceId=_SignalingInterfaceId_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,400,1,100),_SignalingInterfaceId_Type())
signalingInterfaceId.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingInterfaceId.setStatus(_A)
class _SignalingInterfaceName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_SignalingInterfaceName_Type.__name__=_E
_SignalingInterfaceName_Object=MibTableColumn
signalingInterfaceName=_SignalingInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,400,1,200),_SignalingInterfaceName_Type())
signalingInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:signalingInterfaceName.setStatus(_A)
class _SignalingInterfaceNetworkInterface_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_SignalingInterfaceNetworkInterface_Type.__name__=_E
_SignalingInterfaceNetworkInterface_Object=MibTableColumn
signalingInterfaceNetworkInterface=_SignalingInterfaceNetworkInterface_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,400,1,300),_SignalingInterfaceNetworkInterface_Type())
signalingInterfaceNetworkInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:signalingInterfaceNetworkInterface.setStatus(_A)
class _SignalingInterfacePort_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SignalingInterfacePort_Type.__name__=_F
_SignalingInterfacePort_Object=MibTableColumn
signalingInterfacePort=_SignalingInterfacePort_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,400,1,400),_SignalingInterfacePort_Type())
signalingInterfacePort.setMaxAccess(_C)
if mibBuilder.loadTexts:signalingInterfacePort.setStatus(_A)
class _SignalingInterfaceSecurePort_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SignalingInterfaceSecurePort_Type.__name__=_F
_SignalingInterfaceSecurePort_Object=MibTableColumn
signalingInterfaceSecurePort=_SignalingInterfaceSecurePort_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,400,1,450),_SignalingInterfaceSecurePort_Type())
signalingInterfaceSecurePort.setMaxAccess(_C)
if mibBuilder.loadTexts:signalingInterfaceSecurePort.setStatus(_A)
class _SignalingInterfaceTlsMode_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('both',100),(_b,200),(_c,300)))
_SignalingInterfaceTlsMode_Type.__name__=_D
_SignalingInterfaceTlsMode_Object=MibTableColumn
signalingInterfaceTlsMode=_SignalingInterfaceTlsMode_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,400,1,475),_SignalingInterfaceTlsMode_Type())
signalingInterfaceTlsMode.setMaxAccess(_C)
if mibBuilder.loadTexts:signalingInterfaceTlsMode.setStatus(_A)
class _SignalingInterfaceAllowedTransports_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('all',100),(_d,200)))
_SignalingInterfaceAllowedTransports_Type.__name__=_D
_SignalingInterfaceAllowedTransports_Object=MibTableColumn
signalingInterfaceAllowedTransports=_SignalingInterfaceAllowedTransports_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,400,1,480),_SignalingInterfaceAllowedTransports_Type())
signalingInterfaceAllowedTransports.setMaxAccess(_C)
if mibBuilder.loadTexts:signalingInterfaceAllowedTransports.setStatus(_A)
class _SignalingInterfacePublicIpAddr_Type(MxIpAddress):defaultValue=OctetString('')
_SignalingInterfacePublicIpAddr_Type.__name__=_L
_SignalingInterfacePublicIpAddr_Object=MibTableColumn
signalingInterfacePublicIpAddr=_SignalingInterfacePublicIpAddr_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,400,1,500),_SignalingInterfacePublicIpAddr_Type())
signalingInterfacePublicIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:signalingInterfacePublicIpAddr.setStatus(_A)
class _SignalingInterfaceTcpConnectTimeout_Type(Unsigned32):defaultValue=10000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127000))
_SignalingInterfaceTcpConnectTimeout_Type.__name__=_F
_SignalingInterfaceTcpConnectTimeout_Object=MibTableColumn
signalingInterfaceTcpConnectTimeout=_SignalingInterfaceTcpConnectTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,400,1,600),_SignalingInterfaceTcpConnectTimeout_Type())
signalingInterfaceTcpConnectTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:signalingInterfaceTcpConnectTimeout.setStatus(_A)
class _SignalingInterfaceTcpIdleTimeout_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300000))
_SignalingInterfaceTcpIdleTimeout_Type.__name__=_F
_SignalingInterfaceTcpIdleTimeout_Object=MibTableColumn
signalingInterfaceTcpIdleTimeout=_SignalingInterfaceTcpIdleTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,400,1,700),_SignalingInterfaceTcpIdleTimeout_Type())
signalingInterfaceTcpIdleTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:signalingInterfaceTcpIdleTimeout.setStatus(_A)
class _SignalingInterfaceConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,350,380,400)));namedValues=NamedValues(*((_H,100),(_e,200),(_f,300),('invalidTlsMode',350),('invalidTransportMode',380),(_I,400)))
_SignalingInterfaceConfigStatus_Type.__name__=_D
_SignalingInterfaceConfigStatus_Object=MibTableColumn
signalingInterfaceConfigStatus=_SignalingInterfaceConfigStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,400,1,800),_SignalingInterfaceConfigStatus_Type())
signalingInterfaceConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingInterfaceConfigStatus.setStatus(_A)
class _SignalingInterfaceDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_J,0),(_K,10)))
_SignalingInterfaceDelete_Type.__name__=_D
_SignalingInterfaceDelete_Object=MibTableColumn
signalingInterfaceDelete=_SignalingInterfaceDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,400,1,10000),_SignalingInterfaceDelete_Type())
signalingInterfaceDelete.setMaxAccess(_C)
if mibBuilder.loadTexts:signalingInterfaceDelete.setStatus(_A)
_MediaInterfaceTable_Object=MibTable
mediaInterfaceTable=_MediaInterfaceTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,500))
if mibBuilder.loadTexts:mediaInterfaceTable.setStatus(_A)
_MediaInterfaceEntry_Object=MibTableRow
mediaInterfaceEntry=_MediaInterfaceEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,500,1))
mediaInterfaceEntry.setIndexNames((0,_G,_g))
if mibBuilder.loadTexts:mediaInterfaceEntry.setStatus(_A)
class _MediaInterfaceId_Type(Unsigned32):defaultValue=0
_MediaInterfaceId_Type.__name__=_F
_MediaInterfaceId_Object=MibTableColumn
mediaInterfaceId=_MediaInterfaceId_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,500,1,100),_MediaInterfaceId_Type())
mediaInterfaceId.setMaxAccess(_B)
if mibBuilder.loadTexts:mediaInterfaceId.setStatus(_A)
class _MediaInterfaceName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_MediaInterfaceName_Type.__name__=_E
_MediaInterfaceName_Object=MibTableColumn
mediaInterfaceName=_MediaInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,500,1,200),_MediaInterfaceName_Type())
mediaInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:mediaInterfaceName.setStatus(_A)
class _MediaInterfaceNetworkInterface_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_MediaInterfaceNetworkInterface_Type.__name__=_E
_MediaInterfaceNetworkInterface_Object=MibTableColumn
mediaInterfaceNetworkInterface=_MediaInterfaceNetworkInterface_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,500,1,300),_MediaInterfaceNetworkInterface_Type())
mediaInterfaceNetworkInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:mediaInterfaceNetworkInterface.setStatus(_A)
class _MediaInterfacePortRange_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_MediaInterfacePortRange_Type.__name__=_E
_MediaInterfacePortRange_Object=MibTableColumn
mediaInterfacePortRange=_MediaInterfacePortRange_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,500,1,400),_MediaInterfacePortRange_Type())
mediaInterfacePortRange.setMaxAccess(_C)
if mibBuilder.loadTexts:mediaInterfacePortRange.setStatus(_A)
class _MediaInterfacePublicIpAddr_Type(MxIpAddress):defaultValue=OctetString('')
_MediaInterfacePublicIpAddr_Type.__name__=_L
_MediaInterfacePublicIpAddr_Object=MibTableColumn
mediaInterfacePublicIpAddr=_MediaInterfacePublicIpAddr_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,500,1,500),_MediaInterfacePublicIpAddr_Type())
mediaInterfacePublicIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:mediaInterfacePublicIpAddr.setStatus(_A)
class _MediaInterfaceConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*((_H,100),(_e,200),(_f,300),(_I,400)))
_MediaInterfaceConfigStatus_Type.__name__=_D
_MediaInterfaceConfigStatus_Object=MibTableColumn
mediaInterfaceConfigStatus=_MediaInterfaceConfigStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,500,1,600),_MediaInterfaceConfigStatus_Type())
mediaInterfaceConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mediaInterfaceConfigStatus.setStatus(_A)
class _MediaInterfaceDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_J,0),(_K,10)))
_MediaInterfaceDelete_Type.__name__=_D
_MediaInterfaceDelete_Object=MibTableColumn
mediaInterfaceDelete=_MediaInterfaceDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,500,1,10000),_MediaInterfaceDelete_Type())
mediaInterfaceDelete.setMaxAccess(_C)
if mibBuilder.loadTexts:mediaInterfaceDelete.setStatus(_A)
_RegistrationAgentTable_Object=MibTable
registrationAgentTable=_RegistrationAgentTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,600))
if mibBuilder.loadTexts:registrationAgentTable.setStatus(_A)
_RegistrationAgentEntry_Object=MibTableRow
registrationAgentEntry=_RegistrationAgentEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,600,1))
registrationAgentEntry.setIndexNames((0,_G,_h))
if mibBuilder.loadTexts:registrationAgentEntry.setStatus(_A)
class _RegistrationAgentId_Type(Unsigned32):defaultValue=0
_RegistrationAgentId_Type.__name__=_F
_RegistrationAgentId_Object=MibTableColumn
registrationAgentId=_RegistrationAgentId_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,600,1,100),_RegistrationAgentId_Type())
registrationAgentId.setMaxAccess(_B)
if mibBuilder.loadTexts:registrationAgentId.setStatus(_A)
class _RegistrationAgentUsername_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_RegistrationAgentUsername_Type.__name__=_E
_RegistrationAgentUsername_Object=MibTableColumn
registrationAgentUsername=_RegistrationAgentUsername_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,600,1,200),_RegistrationAgentUsername_Type())
registrationAgentUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:registrationAgentUsername.setStatus(_A)
class _RegistrationAgentDomain_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_RegistrationAgentDomain_Type.__name__=_E
_RegistrationAgentDomain_Object=MibTableColumn
registrationAgentDomain=_RegistrationAgentDomain_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,600,1,300),_RegistrationAgentDomain_Type())
registrationAgentDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:registrationAgentDomain.setStatus(_A)
class _RegistrationAgentFriendlyName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_RegistrationAgentFriendlyName_Type.__name__=_E
_RegistrationAgentFriendlyName_Object=MibTableColumn
registrationAgentFriendlyName=_RegistrationAgentFriendlyName_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,600,1,400),_RegistrationAgentFriendlyName_Type())
registrationAgentFriendlyName.setMaxAccess(_C)
if mibBuilder.loadTexts:registrationAgentFriendlyName.setStatus(_A)
class _RegistrationAgentContact_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_RegistrationAgentContact_Type.__name__=_E
_RegistrationAgentContact_Object=MibTableColumn
registrationAgentContact=_RegistrationAgentContact_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,600,1,500),_RegistrationAgentContact_Type())
registrationAgentContact.setMaxAccess(_C)
if mibBuilder.loadTexts:registrationAgentContact.setStatus(_A)
class _RegistrationAgentRegistrationType_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('normal',100),('rFC6140',200)))
_RegistrationAgentRegistrationType_Type.__name__=_D
_RegistrationAgentRegistrationType_Object=MibTableColumn
registrationAgentRegistrationType=_RegistrationAgentRegistrationType_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,600,1,550),_RegistrationAgentRegistrationType_Type())
registrationAgentRegistrationType.setMaxAccess(_C)
if mibBuilder.loadTexts:registrationAgentRegistrationType.setStatus(_A)
class _RegistrationAgentExpireValue_Type(Unsigned32):defaultValue=3600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_RegistrationAgentExpireValue_Type.__name__=_F
_RegistrationAgentExpireValue_Object=MibTableColumn
registrationAgentExpireValue=_RegistrationAgentExpireValue_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,600,1,600),_RegistrationAgentExpireValue_Type())
registrationAgentExpireValue.setMaxAccess(_C)
if mibBuilder.loadTexts:registrationAgentExpireValue.setStatus(_A)
class _RegistrationAgentRetryInterval_Type(Unsigned32):defaultValue=600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_RegistrationAgentRetryInterval_Type.__name__=_F
_RegistrationAgentRetryInterval_Object=MibTableColumn
registrationAgentRetryInterval=_RegistrationAgentRetryInterval_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,600,1,700),_RegistrationAgentRetryInterval_Type())
registrationAgentRetryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:registrationAgentRetryInterval.setStatus(_A)
class _RegistrationAgentConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_H,100),(_I,200),('invalidContact',300)))
_RegistrationAgentConfigStatus_Type.__name__=_D
_RegistrationAgentConfigStatus_Object=MibTableColumn
registrationAgentConfigStatus=_RegistrationAgentConfigStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,600,1,800),_RegistrationAgentConfigStatus_Type())
registrationAgentConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:registrationAgentConfigStatus.setStatus(_A)
class _RegistrationAgentDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_J,0),(_K,10)))
_RegistrationAgentDelete_Type.__name__=_D
_RegistrationAgentDelete_Object=MibTableColumn
registrationAgentDelete=_RegistrationAgentDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,600,1,10000),_RegistrationAgentDelete_Type())
registrationAgentDelete.setMaxAccess(_C)
if mibBuilder.loadTexts:registrationAgentDelete.setStatus(_A)
_PeerMonitoringTable_Object=MibTable
peerMonitoringTable=_PeerMonitoringTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,700))
if mibBuilder.loadTexts:peerMonitoringTable.setStatus(_A)
_PeerMonitoringEntry_Object=MibTableRow
peerMonitoringEntry=_PeerMonitoringEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,700,1))
peerMonitoringEntry.setIndexNames((0,_G,_i))
if mibBuilder.loadTexts:peerMonitoringEntry.setStatus(_A)
class _PeerMonitoringId_Type(Unsigned32):defaultValue=0
_PeerMonitoringId_Type.__name__=_F
_PeerMonitoringId_Object=MibTableColumn
peerMonitoringId=_PeerMonitoringId_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,700,1,100),_PeerMonitoringId_Type())
peerMonitoringId.setMaxAccess(_B)
if mibBuilder.loadTexts:peerMonitoringId.setStatus(_A)
class _PeerMonitoringKeepAliveInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_PeerMonitoringKeepAliveInterval_Type.__name__=_F
_PeerMonitoringKeepAliveInterval_Object=MibTableColumn
peerMonitoringKeepAliveInterval=_PeerMonitoringKeepAliveInterval_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,700,1,200),_PeerMonitoringKeepAliveInterval_Type())
peerMonitoringKeepAliveInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:peerMonitoringKeepAliveInterval.setStatus(_A)
class _PeerMonitoringBlackListingDuration_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_PeerMonitoringBlackListingDuration_Type.__name__=_F
_PeerMonitoringBlackListingDuration_Object=MibTableColumn
peerMonitoringBlackListingDuration=_PeerMonitoringBlackListingDuration_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,700,1,300),_PeerMonitoringBlackListingDuration_Type())
peerMonitoringBlackListingDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:peerMonitoringBlackListingDuration.setStatus(_A)
class _PeerMonitoringBlackListingDelay_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60000))
_PeerMonitoringBlackListingDelay_Type.__name__=_F
_PeerMonitoringBlackListingDelay_Object=MibTableColumn
peerMonitoringBlackListingDelay=_PeerMonitoringBlackListingDelay_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,700,1,400),_PeerMonitoringBlackListingDelay_Type())
peerMonitoringBlackListingDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:peerMonitoringBlackListingDelay.setStatus(_A)
class _PeerMonitoringBlackListingErrorCodes_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,200))
_PeerMonitoringBlackListingErrorCodes_Type.__name__=_E
_PeerMonitoringBlackListingErrorCodes_Object=MibTableColumn
peerMonitoringBlackListingErrorCodes=_PeerMonitoringBlackListingErrorCodes_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,700,1,500),_PeerMonitoringBlackListingErrorCodes_Type())
peerMonitoringBlackListingErrorCodes.setMaxAccess(_C)
if mibBuilder.loadTexts:peerMonitoringBlackListingErrorCodes.setStatus(_A)
class _ConfigModifiedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('yes',100),('no',200)))
_ConfigModifiedStatus_Type.__name__=_D
_ConfigModifiedStatus_Object=MibScalar
configModifiedStatus=_ConfigModifiedStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,100,800),_ConfigModifiedStatus_Type())
configModifiedStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:configModifiedStatus.setStatus(_A)
_RoutingGroup_ObjectIdentity=ObjectIdentity
routingGroup=_RoutingGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,150))
_PrefixBasedRoutingTable_Object=MibTable
prefixBasedRoutingTable=_PrefixBasedRoutingTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,150,100))
if mibBuilder.loadTexts:prefixBasedRoutingTable.setStatus(_A)
_PrefixBasedRoutingEntry_Object=MibTableRow
prefixBasedRoutingEntry=_PrefixBasedRoutingEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,150,100,1))
prefixBasedRoutingEntry.setIndexNames((0,_G,_j))
if mibBuilder.loadTexts:prefixBasedRoutingEntry.setStatus(_A)
class _PrefixBasedRoutingRuleId_Type(Unsigned32):defaultValue=0
_PrefixBasedRoutingRuleId_Type.__name__=_F
_PrefixBasedRoutingRuleId_Object=MibTableColumn
prefixBasedRoutingRuleId=_PrefixBasedRoutingRuleId_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,150,100,1,100),_PrefixBasedRoutingRuleId_Type())
prefixBasedRoutingRuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:prefixBasedRoutingRuleId.setStatus(_A)
class _PrefixBasedRoutingPrefix_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_PrefixBasedRoutingPrefix_Type.__name__=_E
_PrefixBasedRoutingPrefix_Object=MibTableColumn
prefixBasedRoutingPrefix=_PrefixBasedRoutingPrefix_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,150,100,1,200),_PrefixBasedRoutingPrefix_Type())
prefixBasedRoutingPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:prefixBasedRoutingPrefix.setStatus(_A)
class _PrefixBasedRoutingDestinationCa_Type(Unsigned32):defaultValue=0
_PrefixBasedRoutingDestinationCa_Type.__name__=_F
_PrefixBasedRoutingDestinationCa_Object=MibTableColumn
prefixBasedRoutingDestinationCa=_PrefixBasedRoutingDestinationCa_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,150,100,1,300),_PrefixBasedRoutingDestinationCa_Type())
prefixBasedRoutingDestinationCa.setMaxAccess(_C)
if mibBuilder.loadTexts:prefixBasedRoutingDestinationCa.setStatus(_A)
class _PrefixBasedRoutingRoutingMethod_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('nextHop',100),('outboundProxy',200),('requestUri',300)))
_PrefixBasedRoutingRoutingMethod_Type.__name__=_D
_PrefixBasedRoutingRoutingMethod_Object=MibTableColumn
prefixBasedRoutingRoutingMethod=_PrefixBasedRoutingRoutingMethod_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,150,100,1,400),_PrefixBasedRoutingRoutingMethod_Type())
prefixBasedRoutingRoutingMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:prefixBasedRoutingRoutingMethod.setStatus(_A)
class _PrefixBasedRoutingDestinationOverride_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,200))
_PrefixBasedRoutingDestinationOverride_Type.__name__=_E
_PrefixBasedRoutingDestinationOverride_Object=MibTableColumn
prefixBasedRoutingDestinationOverride=_PrefixBasedRoutingDestinationOverride_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,150,100,1,500),_PrefixBasedRoutingDestinationOverride_Type())
prefixBasedRoutingDestinationOverride.setMaxAccess(_C)
if mibBuilder.loadTexts:prefixBasedRoutingDestinationOverride.setStatus(_A)
class _PrefixBasedRoutingRUriHandling_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_M,100),('update',200),('replace',300)))
_PrefixBasedRoutingRUriHandling_Type.__name__=_D
_PrefixBasedRoutingRUriHandling_Object=MibTableColumn
prefixBasedRoutingRUriHandling=_PrefixBasedRoutingRUriHandling_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,150,100,1,600),_PrefixBasedRoutingRUriHandling_Type())
prefixBasedRoutingRUriHandling.setMaxAccess(_C)
if mibBuilder.loadTexts:prefixBasedRoutingRUriHandling.setStatus(_A)
class _PrefixBasedRoutingForceTransport_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*((_M,100),('tCP',200),('uDP',300),('tLS',400)))
_PrefixBasedRoutingForceTransport_Type.__name__=_D
_PrefixBasedRoutingForceTransport_Object=MibTableColumn
prefixBasedRoutingForceTransport=_PrefixBasedRoutingForceTransport_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,150,100,1,700),_PrefixBasedRoutingForceTransport_Type())
prefixBasedRoutingForceTransport.setMaxAccess(_C)
if mibBuilder.loadTexts:prefixBasedRoutingForceTransport.setStatus(_A)
class _PrefixBasedRoutingConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700)));namedValues=NamedValues(*((_H,100),('invalidCa',200),('noPrefix',300),('invalidDestination',400),('destinationOverrideMandatory',500),('prefixDuplicate',600),(_I,700)))
_PrefixBasedRoutingConfigStatus_Type.__name__=_D
_PrefixBasedRoutingConfigStatus_Object=MibTableColumn
prefixBasedRoutingConfigStatus=_PrefixBasedRoutingConfigStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,150,100,1,1000),_PrefixBasedRoutingConfigStatus_Type())
prefixBasedRoutingConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:prefixBasedRoutingConfigStatus.setStatus(_A)
class _PrefixBasedRoutingDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_J,0),(_K,10)))
_PrefixBasedRoutingDelete_Type.__name__=_D
_PrefixBasedRoutingDelete_Object=MibTableColumn
prefixBasedRoutingDelete=_PrefixBasedRoutingDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,150,100,1,10000),_PrefixBasedRoutingDelete_Type())
prefixBasedRoutingDelete.setMaxAccess(_C)
if mibBuilder.loadTexts:prefixBasedRoutingDelete.setStatus(_A)
_RegistrationGroup_ObjectIdentity=ObjectIdentity
registrationGroup=_RegistrationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,170))
_StaticRegistrationTable_Object=MibTable
staticRegistrationTable=_StaticRegistrationTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,170,100))
if mibBuilder.loadTexts:staticRegistrationTable.setStatus(_A)
_StaticRegistrationEntry_Object=MibTableRow
staticRegistrationEntry=_StaticRegistrationEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,170,100,1))
staticRegistrationEntry.setIndexNames((0,_G,_k))
if mibBuilder.loadTexts:staticRegistrationEntry.setStatus(_A)
class _StaticRegistrationRegistrationId_Type(Unsigned32):defaultValue=0
_StaticRegistrationRegistrationId_Type.__name__=_F
_StaticRegistrationRegistrationId_Object=MibTableColumn
staticRegistrationRegistrationId=_StaticRegistrationRegistrationId_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,170,100,1,100),_StaticRegistrationRegistrationId_Type())
staticRegistrationRegistrationId.setMaxAccess(_B)
if mibBuilder.loadTexts:staticRegistrationRegistrationId.setStatus(_A)
class _StaticRegistrationAor_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_StaticRegistrationAor_Type.__name__=_E
_StaticRegistrationAor_Object=MibTableColumn
staticRegistrationAor=_StaticRegistrationAor_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,170,100,1,200),_StaticRegistrationAor_Type())
staticRegistrationAor.setMaxAccess(_C)
if mibBuilder.loadTexts:staticRegistrationAor.setStatus(_A)
class _StaticRegistrationContact_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_StaticRegistrationContact_Type.__name__=_E
_StaticRegistrationContact_Object=MibTableColumn
staticRegistrationContact=_StaticRegistrationContact_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,170,100,1,300),_StaticRegistrationContact_Type())
staticRegistrationContact.setMaxAccess(_C)
if mibBuilder.loadTexts:staticRegistrationContact.setStatus(_A)
class _StaticRegistrationConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_H,100),('aorDuplicate',200),(_I,300)))
_StaticRegistrationConfigStatus_Type.__name__=_D
_StaticRegistrationConfigStatus_Object=MibTableColumn
staticRegistrationConfigStatus=_StaticRegistrationConfigStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,170,100,1,1000),_StaticRegistrationConfigStatus_Type())
staticRegistrationConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:staticRegistrationConfigStatus.setStatus(_A)
class _StaticRegistrationDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_J,0),(_K,10)))
_StaticRegistrationDelete_Type.__name__=_D
_StaticRegistrationDelete_Object=MibTableColumn
staticRegistrationDelete=_StaticRegistrationDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,170,100,1,10000),_StaticRegistrationDelete_Type())
staticRegistrationDelete.setMaxAccess(_C)
if mibBuilder.loadTexts:staticRegistrationDelete.setStatus(_A)
_StatusGroup_ObjectIdentity=ObjectIdentity
statusGroup=_StatusGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200))
_CallAgentStatusTable_Object=MibTable
callAgentStatusTable=_CallAgentStatusTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,100))
if mibBuilder.loadTexts:callAgentStatusTable.setStatus(_A)
_CallAgentStatusEntry_Object=MibTableRow
callAgentStatusEntry=_CallAgentStatusEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,100,1))
callAgentStatusEntry.setIndexNames((0,_G,_l))
if mibBuilder.loadTexts:callAgentStatusEntry.setStatus(_A)
_CallAgentStatusId_Type=Unsigned32
_CallAgentStatusId_Object=MibTableColumn
callAgentStatusId=_CallAgentStatusId_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,100,1,100),_CallAgentStatusId_Type())
callAgentStatusId.setMaxAccess(_B)
if mibBuilder.loadTexts:callAgentStatusId.setStatus(_A)
class _CallAgentStatusName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_CallAgentStatusName_Type.__name__=_E
_CallAgentStatusName_Object=MibTableColumn
callAgentStatusName=_CallAgentStatusName_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,100,1,200),_CallAgentStatusName_Type())
callAgentStatusName.setMaxAccess(_B)
if mibBuilder.loadTexts:callAgentStatusName.setStatus(_A)
_CallAgentStatusSignalingInterface_Type=Unsigned32
_CallAgentStatusSignalingInterface_Object=MibTableColumn
callAgentStatusSignalingInterface=_CallAgentStatusSignalingInterface_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,100,1,300),_CallAgentStatusSignalingInterface_Type())
callAgentStatusSignalingInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:callAgentStatusSignalingInterface.setStatus(_A)
_CallAgentStatusMediaInterface_Type=OctetString
_CallAgentStatusMediaInterface_Object=MibTableColumn
callAgentStatusMediaInterface=_CallAgentStatusMediaInterface_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,100,1,400),_CallAgentStatusMediaInterface_Type())
callAgentStatusMediaInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:callAgentStatusMediaInterface.setStatus(_A)
class _CallAgentStatusGateway_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_CallAgentStatusGateway_Type.__name__=_E
_CallAgentStatusGateway_Object=MibTableColumn
callAgentStatusGateway=_CallAgentStatusGateway_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,100,1,500),_CallAgentStatusGateway_Type())
callAgentStatusGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:callAgentStatusGateway.setStatus(_A)
_CallAgentStatusPeerHost_Type=MxIpAddress
_CallAgentStatusPeerHost_Object=MibTableColumn
callAgentStatusPeerHost=_CallAgentStatusPeerHost_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,100,1,600),_CallAgentStatusPeerHost_Type())
callAgentStatusPeerHost.setMaxAccess(_B)
if mibBuilder.loadTexts:callAgentStatusPeerHost.setStatus(_A)
class _CallAgentStatusState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*((_N,100),(_O,200),('internalError',300),('peerDown',400)))
_CallAgentStatusState_Type.__name__=_D
_CallAgentStatusState_Object=MibTableColumn
callAgentStatusState=_CallAgentStatusState_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,100,1,700),_CallAgentStatusState_Type())
callAgentStatusState.setMaxAccess(_B)
if mibBuilder.loadTexts:callAgentStatusState.setStatus(_A)
_SignalingInterfaceStatusTable_Object=MibTable
signalingInterfaceStatusTable=_SignalingInterfaceStatusTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,200))
if mibBuilder.loadTexts:signalingInterfaceStatusTable.setStatus(_A)
_SignalingInterfaceStatusEntry_Object=MibTableRow
signalingInterfaceStatusEntry=_SignalingInterfaceStatusEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,200,1))
signalingInterfaceStatusEntry.setIndexNames((0,_G,_m))
if mibBuilder.loadTexts:signalingInterfaceStatusEntry.setStatus(_A)
_SignalingInterfaceStatusId_Type=Unsigned32
_SignalingInterfaceStatusId_Object=MibTableColumn
signalingInterfaceStatusId=_SignalingInterfaceStatusId_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,200,1,100),_SignalingInterfaceStatusId_Type())
signalingInterfaceStatusId.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingInterfaceStatusId.setStatus(_A)
class _SignalingInterfaceStatusName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_SignalingInterfaceStatusName_Type.__name__=_E
_SignalingInterfaceStatusName_Object=MibTableColumn
signalingInterfaceStatusName=_SignalingInterfaceStatusName_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,200,1,200),_SignalingInterfaceStatusName_Type())
signalingInterfaceStatusName.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingInterfaceStatusName.setStatus(_A)
_SignalingInterfaceStatusNetworkInterface_Type=OctetString
_SignalingInterfaceStatusNetworkInterface_Object=MibTableColumn
signalingInterfaceStatusNetworkInterface=_SignalingInterfaceStatusNetworkInterface_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,200,1,300),_SignalingInterfaceStatusNetworkInterface_Type())
signalingInterfaceStatusNetworkInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingInterfaceStatusNetworkInterface.setStatus(_A)
_SignalingInterfaceStatusPort_Type=Unsigned32
_SignalingInterfaceStatusPort_Object=MibTableColumn
signalingInterfaceStatusPort=_SignalingInterfaceStatusPort_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,200,1,400),_SignalingInterfaceStatusPort_Type())
signalingInterfaceStatusPort.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingInterfaceStatusPort.setStatus(_A)
_SignalingInterfaceStatusSecurePort_Type=Unsigned32
_SignalingInterfaceStatusSecurePort_Object=MibTableColumn
signalingInterfaceStatusSecurePort=_SignalingInterfaceStatusSecurePort_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,200,1,450),_SignalingInterfaceStatusSecurePort_Type())
signalingInterfaceStatusSecurePort.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingInterfaceStatusSecurePort.setStatus(_A)
class _SignalingInterfaceStatusTlsMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('both',100),(_b,200),(_c,300)))
_SignalingInterfaceStatusTlsMode_Type.__name__=_D
_SignalingInterfaceStatusTlsMode_Object=MibTableColumn
signalingInterfaceStatusTlsMode=_SignalingInterfaceStatusTlsMode_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,200,1,475),_SignalingInterfaceStatusTlsMode_Type())
signalingInterfaceStatusTlsMode.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingInterfaceStatusTlsMode.setStatus(_A)
class _SignalingInterfaceStatusAllowedTransports_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('all',100),(_d,200)))
_SignalingInterfaceStatusAllowedTransports_Type.__name__=_D
_SignalingInterfaceStatusAllowedTransports_Object=MibTableColumn
signalingInterfaceStatusAllowedTransports=_SignalingInterfaceStatusAllowedTransports_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,200,1,485),_SignalingInterfaceStatusAllowedTransports_Type())
signalingInterfaceStatusAllowedTransports.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingInterfaceStatusAllowedTransports.setStatus(_A)
_SignalingInterfaceStatusPublicIpAddr_Type=MxIpAddress
_SignalingInterfaceStatusPublicIpAddr_Object=MibTableColumn
signalingInterfaceStatusPublicIpAddr=_SignalingInterfaceStatusPublicIpAddr_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,200,1,500),_SignalingInterfaceStatusPublicIpAddr_Type())
signalingInterfaceStatusPublicIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingInterfaceStatusPublicIpAddr.setStatus(_A)
_SignalingInterfaceStatusTcpConnectTimeout_Type=Unsigned32
_SignalingInterfaceStatusTcpConnectTimeout_Object=MibTableColumn
signalingInterfaceStatusTcpConnectTimeout=_SignalingInterfaceStatusTcpConnectTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,200,1,600),_SignalingInterfaceStatusTcpConnectTimeout_Type())
signalingInterfaceStatusTcpConnectTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingInterfaceStatusTcpConnectTimeout.setStatus(_A)
_SignalingInterfaceStatusTcpIdleTimeout_Type=Unsigned32
_SignalingInterfaceStatusTcpIdleTimeout_Object=MibTableColumn
signalingInterfaceStatusTcpIdleTimeout=_SignalingInterfaceStatusTcpIdleTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,200,1,700),_SignalingInterfaceStatusTcpIdleTimeout_Type())
signalingInterfaceStatusTcpIdleTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingInterfaceStatusTcpIdleTimeout.setStatus(_A)
_SignalingInterfaceStatusIpAddress_Type=MxIpAddress
_SignalingInterfaceStatusIpAddress_Object=MibTableColumn
signalingInterfaceStatusIpAddress=_SignalingInterfaceStatusIpAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,200,1,800),_SignalingInterfaceStatusIpAddress_Type())
signalingInterfaceStatusIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingInterfaceStatusIpAddress.setStatus(_A)
class _SignalingInterfaceStatusState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_N,100),(_O,200),(_n,300)))
_SignalingInterfaceStatusState_Type.__name__=_D
_SignalingInterfaceStatusState_Object=MibTableColumn
signalingInterfaceStatusState=_SignalingInterfaceStatusState_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,200,1,900),_SignalingInterfaceStatusState_Type())
signalingInterfaceStatusState.setMaxAccess(_B)
if mibBuilder.loadTexts:signalingInterfaceStatusState.setStatus(_A)
_MediaInterfaceStatusTable_Object=MibTable
mediaInterfaceStatusTable=_MediaInterfaceStatusTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,300))
if mibBuilder.loadTexts:mediaInterfaceStatusTable.setStatus(_A)
_MediaInterfaceStatusEntry_Object=MibTableRow
mediaInterfaceStatusEntry=_MediaInterfaceStatusEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,300,1))
mediaInterfaceStatusEntry.setIndexNames((0,_G,_o))
if mibBuilder.loadTexts:mediaInterfaceStatusEntry.setStatus(_A)
_MediaInterfaceStatusId_Type=Unsigned32
_MediaInterfaceStatusId_Object=MibTableColumn
mediaInterfaceStatusId=_MediaInterfaceStatusId_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,300,1,100),_MediaInterfaceStatusId_Type())
mediaInterfaceStatusId.setMaxAccess(_B)
if mibBuilder.loadTexts:mediaInterfaceStatusId.setStatus(_A)
class _MediaInterfaceStatusName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_MediaInterfaceStatusName_Type.__name__=_E
_MediaInterfaceStatusName_Object=MibTableColumn
mediaInterfaceStatusName=_MediaInterfaceStatusName_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,300,1,200),_MediaInterfaceStatusName_Type())
mediaInterfaceStatusName.setMaxAccess(_B)
if mibBuilder.loadTexts:mediaInterfaceStatusName.setStatus(_A)
_MediaInterfaceStatusNetworkInterface_Type=OctetString
_MediaInterfaceStatusNetworkInterface_Object=MibTableColumn
mediaInterfaceStatusNetworkInterface=_MediaInterfaceStatusNetworkInterface_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,300,1,300),_MediaInterfaceStatusNetworkInterface_Type())
mediaInterfaceStatusNetworkInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:mediaInterfaceStatusNetworkInterface.setStatus(_A)
class _MediaInterfaceStatusPortRange_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_MediaInterfaceStatusPortRange_Type.__name__=_E
_MediaInterfaceStatusPortRange_Object=MibTableColumn
mediaInterfaceStatusPortRange=_MediaInterfaceStatusPortRange_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,300,1,400),_MediaInterfaceStatusPortRange_Type())
mediaInterfaceStatusPortRange.setMaxAccess(_B)
if mibBuilder.loadTexts:mediaInterfaceStatusPortRange.setStatus(_A)
_MediaInterfaceStatusPublicIpAddr_Type=MxIpAddress
_MediaInterfaceStatusPublicIpAddr_Object=MibTableColumn
mediaInterfaceStatusPublicIpAddr=_MediaInterfaceStatusPublicIpAddr_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,300,1,500),_MediaInterfaceStatusPublicIpAddr_Type())
mediaInterfaceStatusPublicIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mediaInterfaceStatusPublicIpAddr.setStatus(_A)
_MediaInterfaceStatusIpAddress_Type=MxIpAddress
_MediaInterfaceStatusIpAddress_Object=MibTableColumn
mediaInterfaceStatusIpAddress=_MediaInterfaceStatusIpAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,300,1,600),_MediaInterfaceStatusIpAddress_Type())
mediaInterfaceStatusIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mediaInterfaceStatusIpAddress.setStatus(_A)
class _MediaInterfaceStatusState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_N,100),(_O,200),(_n,300)))
_MediaInterfaceStatusState_Type.__name__=_D
_MediaInterfaceStatusState_Object=MibTableColumn
mediaInterfaceStatusState=_MediaInterfaceStatusState_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,300,1,700),_MediaInterfaceStatusState_Type())
mediaInterfaceStatusState.setMaxAccess(_B)
if mibBuilder.loadTexts:mediaInterfaceStatusState.setStatus(_A)
_CallAgentRulesetStatusTable_Object=MibTable
callAgentRulesetStatusTable=_CallAgentRulesetStatusTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,400))
if mibBuilder.loadTexts:callAgentRulesetStatusTable.setStatus(_A)
_CallAgentRulesetStatusEntry_Object=MibTableRow
callAgentRulesetStatusEntry=_CallAgentRulesetStatusEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,400,1))
callAgentRulesetStatusEntry.setIndexNames((0,_G,_p))
if mibBuilder.loadTexts:callAgentRulesetStatusEntry.setStatus(_A)
_CallAgentRulesetStatusId_Type=Unsigned32
_CallAgentRulesetStatusId_Object=MibTableColumn
callAgentRulesetStatusId=_CallAgentRulesetStatusId_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,400,1,100),_CallAgentRulesetStatusId_Type())
callAgentRulesetStatusId.setMaxAccess(_B)
if mibBuilder.loadTexts:callAgentRulesetStatusId.setStatus(_A)
_CallAgentRulesetStatusCallAgent_Type=Unsigned32
_CallAgentRulesetStatusCallAgent_Object=MibTableColumn
callAgentRulesetStatusCallAgent=_CallAgentRulesetStatusCallAgent_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,400,1,200),_CallAgentRulesetStatusCallAgent_Type())
callAgentRulesetStatusCallAgent.setMaxAccess(_B)
if mibBuilder.loadTexts:callAgentRulesetStatusCallAgent.setStatus(_A)
_CallAgentRulesetStatusPriority_Type=Unsigned32
_CallAgentRulesetStatusPriority_Object=MibTableColumn
callAgentRulesetStatusPriority=_CallAgentRulesetStatusPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,400,1,300),_CallAgentRulesetStatusPriority_Type())
callAgentRulesetStatusPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:callAgentRulesetStatusPriority.setStatus(_A)
class _CallAgentRulesetStatusRuleset_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_CallAgentRulesetStatusRuleset_Type.__name__=_E
_CallAgentRulesetStatusRuleset_Object=MibTableColumn
callAgentRulesetStatusRuleset=_CallAgentRulesetStatusRuleset_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,400,1,400),_CallAgentRulesetStatusRuleset_Type())
callAgentRulesetStatusRuleset.setMaxAccess(_B)
if mibBuilder.loadTexts:callAgentRulesetStatusRuleset.setStatus(_A)
class _CallAgentRulesetStatusParameters_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_CallAgentRulesetStatusParameters_Type.__name__=_E
_CallAgentRulesetStatusParameters_Object=MibTableColumn
callAgentRulesetStatusParameters=_CallAgentRulesetStatusParameters_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,400,1,500),_CallAgentRulesetStatusParameters_Type())
callAgentRulesetStatusParameters.setMaxAccess(_B)
if mibBuilder.loadTexts:callAgentRulesetStatusParameters.setStatus(_A)
_RoutingRulesStatusTable_Object=MibTable
routingRulesStatusTable=_RoutingRulesStatusTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,500))
if mibBuilder.loadTexts:routingRulesStatusTable.setStatus(_A)
_RoutingRulesStatusEntry_Object=MibTableRow
routingRulesStatusEntry=_RoutingRulesStatusEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,500,1))
routingRulesStatusEntry.setIndexNames((0,_G,_q))
if mibBuilder.loadTexts:routingRulesStatusEntry.setStatus(_A)
_RoutingRulesStatusId_Type=Unsigned32
_RoutingRulesStatusId_Object=MibTableColumn
routingRulesStatusId=_RoutingRulesStatusId_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,500,1,100),_RoutingRulesStatusId_Type())
routingRulesStatusId.setMaxAccess(_B)
if mibBuilder.loadTexts:routingRulesStatusId.setStatus(_A)
_RoutingRulesStatusPriority_Type=Unsigned32
_RoutingRulesStatusPriority_Object=MibTableColumn
routingRulesStatusPriority=_RoutingRulesStatusPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,500,1,200),_RoutingRulesStatusPriority_Type())
routingRulesStatusPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:routingRulesStatusPriority.setStatus(_A)
class _RoutingRulesStatusRuleset_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_RoutingRulesStatusRuleset_Type.__name__=_E
_RoutingRulesStatusRuleset_Object=MibTableColumn
routingRulesStatusRuleset=_RoutingRulesStatusRuleset_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,500,1,300),_RoutingRulesStatusRuleset_Type())
routingRulesStatusRuleset.setMaxAccess(_B)
if mibBuilder.loadTexts:routingRulesStatusRuleset.setStatus(_A)
class _RoutingRulesStatusParameters_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_RoutingRulesStatusParameters_Type.__name__=_E
_RoutingRulesStatusParameters_Object=MibTableColumn
routingRulesStatusParameters=_RoutingRulesStatusParameters_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,500,1,400),_RoutingRulesStatusParameters_Type())
routingRulesStatusParameters.setMaxAccess(_B)
if mibBuilder.loadTexts:routingRulesStatusParameters.setStatus(_A)
_RegistrationAgentStatusTable_Object=MibTable
registrationAgentStatusTable=_RegistrationAgentStatusTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,600))
if mibBuilder.loadTexts:registrationAgentStatusTable.setStatus(_A)
_RegistrationAgentStatusEntry_Object=MibTableRow
registrationAgentStatusEntry=_RegistrationAgentStatusEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,600,1))
registrationAgentStatusEntry.setIndexNames((0,_G,_r))
if mibBuilder.loadTexts:registrationAgentStatusEntry.setStatus(_A)
_RegistrationAgentStatusId_Type=Unsigned32
_RegistrationAgentStatusId_Object=MibTableColumn
registrationAgentStatusId=_RegistrationAgentStatusId_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,600,1,100),_RegistrationAgentStatusId_Type())
registrationAgentStatusId.setMaxAccess(_B)
if mibBuilder.loadTexts:registrationAgentStatusId.setStatus(_A)
class _RegistrationAgentStatusState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(200,300,400,600,800,1000,1100,1200)));namedValues=NamedValues(*(('registering',200),('registered',300),('refreshing',400),('unreachable',600),('rejected',800),('invalidResponse',1000),('notFound',1100),('unknown',1200)))
_RegistrationAgentStatusState_Type.__name__=_D
_RegistrationAgentStatusState_Object=MibTableColumn
registrationAgentStatusState=_RegistrationAgentStatusState_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,200,600,1,200),_RegistrationAgentStatusState_Type())
registrationAgentStatusState.setMaxAccess(_B)
if mibBuilder.loadTexts:registrationAgentStatusState.setStatus(_A)
_StatisticsGroup_ObjectIdentity=ObjectIdentity
statisticsGroup=_StatisticsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,300))
_NbActiveCalls_Type=Unsigned32
_NbActiveCalls_Object=MibScalar
nbActiveCalls=_NbActiveCalls_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,300,100),_NbActiveCalls_Type())
nbActiveCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:nbActiveCalls.setStatus(_A)
_CallAgentStatsTable_Object=MibTable
callAgentStatsTable=_CallAgentStatsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,300,200))
if mibBuilder.loadTexts:callAgentStatsTable.setStatus(_A)
_CallAgentStatsEntry_Object=MibTableRow
callAgentStatsEntry=_CallAgentStatsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,300,200,1))
callAgentStatsEntry.setIndexNames((0,_G,_s))
if mibBuilder.loadTexts:callAgentStatsEntry.setStatus(_A)
_CallAgentStatsCallAgent_Type=Unsigned32
_CallAgentStatsCallAgent_Object=MibTableColumn
callAgentStatsCallAgent=_CallAgentStatsCallAgent_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,300,200,1,100),_CallAgentStatsCallAgent_Type())
callAgentStatsCallAgent.setMaxAccess(_B)
if mibBuilder.loadTexts:callAgentStatsCallAgent.setStatus(_A)
_CallAgentStatsInboundCallAttempts_Type=Unsigned32
_CallAgentStatsInboundCallAttempts_Object=MibTableColumn
callAgentStatsInboundCallAttempts=_CallAgentStatsInboundCallAttempts_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,300,200,1,200),_CallAgentStatsInboundCallAttempts_Type())
callAgentStatsInboundCallAttempts.setMaxAccess(_B)
if mibBuilder.loadTexts:callAgentStatsInboundCallAttempts.setStatus(_A)
_CallAgentStatsOutboundCallAttempts_Type=Unsigned32
_CallAgentStatsOutboundCallAttempts_Object=MibTableColumn
callAgentStatsOutboundCallAttempts=_CallAgentStatsOutboundCallAttempts_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,300,200,1,300),_CallAgentStatsOutboundCallAttempts_Type())
callAgentStatsOutboundCallAttempts.setMaxAccess(_B)
if mibBuilder.loadTexts:callAgentStatsOutboundCallAttempts.setStatus(_A)
_CallAgentStatsInboundCallCompleted_Type=Unsigned32
_CallAgentStatsInboundCallCompleted_Object=MibTableColumn
callAgentStatsInboundCallCompleted=_CallAgentStatsInboundCallCompleted_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,300,200,1,400),_CallAgentStatsInboundCallCompleted_Type())
callAgentStatsInboundCallCompleted.setMaxAccess(_B)
if mibBuilder.loadTexts:callAgentStatsInboundCallCompleted.setStatus(_A)
_CallAgentStatsOutboundCallCompleted_Type=Unsigned32
_CallAgentStatsOutboundCallCompleted_Object=MibTableColumn
callAgentStatsOutboundCallCompleted=_CallAgentStatsOutboundCallCompleted_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,300,200,1,500),_CallAgentStatsOutboundCallCompleted_Type())
callAgentStatsOutboundCallCompleted.setMaxAccess(_B)
if mibBuilder.loadTexts:callAgentStatsOutboundCallCompleted.setStatus(_A)
_TransportGroup_ObjectIdentity=ObjectIdentity
transportGroup=_TransportGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,400))
class _CertificateValidation_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('noValidation',100),('hostName',200)))
_CertificateValidation_Type.__name__=_D
_CertificateValidation_Object=MibScalar
certificateValidation=_CertificateValidation_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,400,100),_CertificateValidation_Type())
certificateValidation.setMaxAccess(_C)
if mibBuilder.loadTexts:certificateValidation.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_D
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_D
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,4400,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'sbcMIB':sbcMIB,'sbcMIBObjects':sbcMIBObjects,'configGroup':configGroup,'callAgentTable':callAgentTable,'callAgentEntry':callAgentEntry,_S:callAgentId,'callAgentName':callAgentName,'callAgentEnable':callAgentEnable,'callAgentSignalingInterface':callAgentSignalingInterface,'callAgentMediaInterface':callAgentMediaInterface,'callAgentGateway':callAgentGateway,'callAgentPeerHost':callAgentPeerHost,'callAgentPeerNetwork':callAgentPeerNetwork,'callAgentForceTransport':callAgentForceTransport,'callAgentConfigStatus':callAgentConfigStatus,'callAgentDelete':callAgentDelete,'callAgentRulesetTable':callAgentRulesetTable,'callAgentRulesetEntry':callAgentRulesetEntry,_T:callAgentRulesetId,'callAgentRulesetCallAgent':callAgentRulesetCallAgent,'callAgentRulesetPriority':callAgentRulesetPriority,'callAgentRulesetRuleset':callAgentRulesetRuleset,'callAgentRulesetParameters':callAgentRulesetParameters,'callAgentRulesetConfigStatus':callAgentRulesetConfigStatus,'callAgentRulesetDelete':callAgentRulesetDelete,'callAgentRulesetCatalogTable':callAgentRulesetCatalogTable,'callAgentRulesetCatalogEntry':callAgentRulesetCatalogEntry,_V:callAgentRulesetCatalogId,'callAgentRulesetCatalogName':callAgentRulesetCatalogName,'callAgentRulesetCatalogDescription':callAgentRulesetCatalogDescription,'callAgentRulesetCatalogOrigin':callAgentRulesetCatalogOrigin,'routingRulesTable':routingRulesTable,'routingRulesEntry':routingRulesEntry,_Y:routingRulesId,'routingRulesPriority':routingRulesPriority,'routingRulesRuleset':routingRulesRuleset,'routingRulesParameters':routingRulesParameters,'routingRulesConfigStatus':routingRulesConfigStatus,'routingRulesDelete':routingRulesDelete,'routingRulesetCatalogTable':routingRulesetCatalogTable,'routingRulesetCatalogEntry':routingRulesetCatalogEntry,_Z:routingRulesetCatalogId,'routingRulesetCatalogName':routingRulesetCatalogName,'routingRulesetCatalogDescription':routingRulesetCatalogDescription,'routingRulesetCatalogOrigin':routingRulesetCatalogOrigin,'signalingInterfaceTable':signalingInterfaceTable,'signalingInterfaceEntry':signalingInterfaceEntry,_a:signalingInterfaceId,'signalingInterfaceName':signalingInterfaceName,'signalingInterfaceNetworkInterface':signalingInterfaceNetworkInterface,'signalingInterfacePort':signalingInterfacePort,'signalingInterfaceSecurePort':signalingInterfaceSecurePort,'signalingInterfaceTlsMode':signalingInterfaceTlsMode,'signalingInterfaceAllowedTransports':signalingInterfaceAllowedTransports,'signalingInterfacePublicIpAddr':signalingInterfacePublicIpAddr,'signalingInterfaceTcpConnectTimeout':signalingInterfaceTcpConnectTimeout,'signalingInterfaceTcpIdleTimeout':signalingInterfaceTcpIdleTimeout,'signalingInterfaceConfigStatus':signalingInterfaceConfigStatus,'signalingInterfaceDelete':signalingInterfaceDelete,'mediaInterfaceTable':mediaInterfaceTable,'mediaInterfaceEntry':mediaInterfaceEntry,_g:mediaInterfaceId,'mediaInterfaceName':mediaInterfaceName,'mediaInterfaceNetworkInterface':mediaInterfaceNetworkInterface,'mediaInterfacePortRange':mediaInterfacePortRange,'mediaInterfacePublicIpAddr':mediaInterfacePublicIpAddr,'mediaInterfaceConfigStatus':mediaInterfaceConfigStatus,'mediaInterfaceDelete':mediaInterfaceDelete,'registrationAgentTable':registrationAgentTable,'registrationAgentEntry':registrationAgentEntry,_h:registrationAgentId,'registrationAgentUsername':registrationAgentUsername,'registrationAgentDomain':registrationAgentDomain,'registrationAgentFriendlyName':registrationAgentFriendlyName,'registrationAgentContact':registrationAgentContact,'registrationAgentRegistrationType':registrationAgentRegistrationType,'registrationAgentExpireValue':registrationAgentExpireValue,'registrationAgentRetryInterval':registrationAgentRetryInterval,'registrationAgentConfigStatus':registrationAgentConfigStatus,'registrationAgentDelete':registrationAgentDelete,'peerMonitoringTable':peerMonitoringTable,'peerMonitoringEntry':peerMonitoringEntry,_i:peerMonitoringId,'peerMonitoringKeepAliveInterval':peerMonitoringKeepAliveInterval,'peerMonitoringBlackListingDuration':peerMonitoringBlackListingDuration,'peerMonitoringBlackListingDelay':peerMonitoringBlackListingDelay,'peerMonitoringBlackListingErrorCodes':peerMonitoringBlackListingErrorCodes,'configModifiedStatus':configModifiedStatus,'routingGroup':routingGroup,'prefixBasedRoutingTable':prefixBasedRoutingTable,'prefixBasedRoutingEntry':prefixBasedRoutingEntry,_j:prefixBasedRoutingRuleId,'prefixBasedRoutingPrefix':prefixBasedRoutingPrefix,'prefixBasedRoutingDestinationCa':prefixBasedRoutingDestinationCa,'prefixBasedRoutingRoutingMethod':prefixBasedRoutingRoutingMethod,'prefixBasedRoutingDestinationOverride':prefixBasedRoutingDestinationOverride,'prefixBasedRoutingRUriHandling':prefixBasedRoutingRUriHandling,'prefixBasedRoutingForceTransport':prefixBasedRoutingForceTransport,'prefixBasedRoutingConfigStatus':prefixBasedRoutingConfigStatus,'prefixBasedRoutingDelete':prefixBasedRoutingDelete,'registrationGroup':registrationGroup,'staticRegistrationTable':staticRegistrationTable,'staticRegistrationEntry':staticRegistrationEntry,_k:staticRegistrationRegistrationId,'staticRegistrationAor':staticRegistrationAor,'staticRegistrationContact':staticRegistrationContact,'staticRegistrationConfigStatus':staticRegistrationConfigStatus,'staticRegistrationDelete':staticRegistrationDelete,'statusGroup':statusGroup,'callAgentStatusTable':callAgentStatusTable,'callAgentStatusEntry':callAgentStatusEntry,_l:callAgentStatusId,'callAgentStatusName':callAgentStatusName,'callAgentStatusSignalingInterface':callAgentStatusSignalingInterface,'callAgentStatusMediaInterface':callAgentStatusMediaInterface,'callAgentStatusGateway':callAgentStatusGateway,'callAgentStatusPeerHost':callAgentStatusPeerHost,'callAgentStatusState':callAgentStatusState,'signalingInterfaceStatusTable':signalingInterfaceStatusTable,'signalingInterfaceStatusEntry':signalingInterfaceStatusEntry,_m:signalingInterfaceStatusId,'signalingInterfaceStatusName':signalingInterfaceStatusName,'signalingInterfaceStatusNetworkInterface':signalingInterfaceStatusNetworkInterface,'signalingInterfaceStatusPort':signalingInterfaceStatusPort,'signalingInterfaceStatusSecurePort':signalingInterfaceStatusSecurePort,'signalingInterfaceStatusTlsMode':signalingInterfaceStatusTlsMode,'signalingInterfaceStatusAllowedTransports':signalingInterfaceStatusAllowedTransports,'signalingInterfaceStatusPublicIpAddr':signalingInterfaceStatusPublicIpAddr,'signalingInterfaceStatusTcpConnectTimeout':signalingInterfaceStatusTcpConnectTimeout,'signalingInterfaceStatusTcpIdleTimeout':signalingInterfaceStatusTcpIdleTimeout,'signalingInterfaceStatusIpAddress':signalingInterfaceStatusIpAddress,'signalingInterfaceStatusState':signalingInterfaceStatusState,'mediaInterfaceStatusTable':mediaInterfaceStatusTable,'mediaInterfaceStatusEntry':mediaInterfaceStatusEntry,_o:mediaInterfaceStatusId,'mediaInterfaceStatusName':mediaInterfaceStatusName,'mediaInterfaceStatusNetworkInterface':mediaInterfaceStatusNetworkInterface,'mediaInterfaceStatusPortRange':mediaInterfaceStatusPortRange,'mediaInterfaceStatusPublicIpAddr':mediaInterfaceStatusPublicIpAddr,'mediaInterfaceStatusIpAddress':mediaInterfaceStatusIpAddress,'mediaInterfaceStatusState':mediaInterfaceStatusState,'callAgentRulesetStatusTable':callAgentRulesetStatusTable,'callAgentRulesetStatusEntry':callAgentRulesetStatusEntry,_p:callAgentRulesetStatusId,'callAgentRulesetStatusCallAgent':callAgentRulesetStatusCallAgent,'callAgentRulesetStatusPriority':callAgentRulesetStatusPriority,'callAgentRulesetStatusRuleset':callAgentRulesetStatusRuleset,'callAgentRulesetStatusParameters':callAgentRulesetStatusParameters,'routingRulesStatusTable':routingRulesStatusTable,'routingRulesStatusEntry':routingRulesStatusEntry,_q:routingRulesStatusId,'routingRulesStatusPriority':routingRulesStatusPriority,'routingRulesStatusRuleset':routingRulesStatusRuleset,'routingRulesStatusParameters':routingRulesStatusParameters,'registrationAgentStatusTable':registrationAgentStatusTable,'registrationAgentStatusEntry':registrationAgentStatusEntry,_r:registrationAgentStatusId,'registrationAgentStatusState':registrationAgentStatusState,'statisticsGroup':statisticsGroup,'nbActiveCalls':nbActiveCalls,'callAgentStatsTable':callAgentStatsTable,'callAgentStatsEntry':callAgentStatsEntry,_s:callAgentStatsCallAgent,'callAgentStatsInboundCallAttempts':callAgentStatsInboundCallAttempts,'callAgentStatsOutboundCallAttempts':callAgentStatsOutboundCallAttempts,'callAgentStatsInboundCallCompleted':callAgentStatsInboundCallCompleted,'callAgentStatsOutboundCallCompleted':callAgentStatsOutboundCallCompleted,'transportGroup':transportGroup,'certificateValidation':certificateValidation,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})