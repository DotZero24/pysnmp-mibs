_N='normalRouting'
_M='bsifnPolicyInterfacePolicyName'
_L='bsifnPolicyInterfaceIndex'
_K='bsifnPolicyName'
_J='InetAddressType'
_I='InetAddress'
_H='not-accessible'
_G='read-only'
_F='SnmpAdminString'
_E='InetPortNumber'
_D='BAY-STACK-IP-FWD-NH-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressPrefixLength,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_I,'InetAddressPrefixLength',_J,_E)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackIpFwdNhMib=ModuleIdentity((1,3,6,1,4,1,45,5,35))
if mibBuilder.loadTexts:bayStackIpFwdNhMib.setRevisions(('2011-04-15 00:00','2010-10-22 00:00','2009-09-30 00:00','2009-09-11 00:00','2009-08-26 00:00','2009-08-21 00:00'))
_BayStackIpFwdNhNotifications_ObjectIdentity=ObjectIdentity
bayStackIpFwdNhNotifications=_BayStackIpFwdNhNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,35,0))
_BayStackIpFwdNhObjects_ObjectIdentity=ObjectIdentity
bayStackIpFwdNhObjects=_BayStackIpFwdNhObjects_ObjectIdentity((1,3,6,1,4,1,45,5,35,1))
_BsifnScalars_ObjectIdentity=ObjectIdentity
bsifnScalars=_BsifnScalars_ObjectIdentity((1,3,6,1,4,1,45,5,35,1,1))
_BsifnIpForwardingNextHopAdminEnabled_Type=TruthValue
_BsifnIpForwardingNextHopAdminEnabled_Object=MibScalar
bsifnIpForwardingNextHopAdminEnabled=_BsifnIpForwardingNextHopAdminEnabled_Object((1,3,6,1,4,1,45,5,35,1,1,1),_BsifnIpForwardingNextHopAdminEnabled_Type())
bsifnIpForwardingNextHopAdminEnabled.setMaxAccess('read-write')
if mibBuilder.loadTexts:bsifnIpForwardingNextHopAdminEnabled.setStatus(_A)
_BsifnIpForwardingNextHopOperEnabled_Type=TruthValue
_BsifnIpForwardingNextHopOperEnabled_Object=MibScalar
bsifnIpForwardingNextHopOperEnabled=_BsifnIpForwardingNextHopOperEnabled_Object((1,3,6,1,4,1,45,5,35,1,1,2),_BsifnIpForwardingNextHopOperEnabled_Type())
bsifnIpForwardingNextHopOperEnabled.setMaxAccess(_G)
if mibBuilder.loadTexts:bsifnIpForwardingNextHopOperEnabled.setStatus(_A)
_BsifnPolicyTable_Object=MibTable
bsifnPolicyTable=_BsifnPolicyTable_Object((1,3,6,1,4,1,45,5,35,1,2))
if mibBuilder.loadTexts:bsifnPolicyTable.setStatus(_A)
_BsifnPolicyEntry_Object=MibTableRow
bsifnPolicyEntry=_BsifnPolicyEntry_Object((1,3,6,1,4,1,45,5,35,1,2,1))
bsifnPolicyEntry.setIndexNames((1,_D,_K))
if mibBuilder.loadTexts:bsifnPolicyEntry.setStatus(_A)
class _BsifnPolicyName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_BsifnPolicyName_Type.__name__=_F
_BsifnPolicyName_Object=MibTableColumn
bsifnPolicyName=_BsifnPolicyName_Object((1,3,6,1,4,1,45,5,35,1,2,1,1),_BsifnPolicyName_Type())
bsifnPolicyName.setMaxAccess(_H)
if mibBuilder.loadTexts:bsifnPolicyName.setStatus(_A)
_BsifnPolicyMatchInetAddressType_Type=InetAddressType
_BsifnPolicyMatchInetAddressType_Object=MibTableColumn
bsifnPolicyMatchInetAddressType=_BsifnPolicyMatchInetAddressType_Object((1,3,6,1,4,1,45,5,35,1,2,1,2),_BsifnPolicyMatchInetAddressType_Type())
bsifnPolicyMatchInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:bsifnPolicyMatchInetAddressType.setStatus(_A)
_BsifnPolicyMatchInetAddress_Type=InetAddress
_BsifnPolicyMatchInetAddress_Object=MibTableColumn
bsifnPolicyMatchInetAddress=_BsifnPolicyMatchInetAddress_Object((1,3,6,1,4,1,45,5,35,1,2,1,3),_BsifnPolicyMatchInetAddress_Type())
bsifnPolicyMatchInetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:bsifnPolicyMatchInetAddress.setStatus(_A)
_BsifnPolicyMatchInetAddressMask_Type=InetAddressPrefixLength
_BsifnPolicyMatchInetAddressMask_Object=MibTableColumn
bsifnPolicyMatchInetAddressMask=_BsifnPolicyMatchInetAddressMask_Object((1,3,6,1,4,1,45,5,35,1,2,1,4),_BsifnPolicyMatchInetAddressMask_Type())
bsifnPolicyMatchInetAddressMask.setMaxAccess(_B)
if mibBuilder.loadTexts:bsifnPolicyMatchInetAddressMask.setStatus(_A)
class _BsifnPolicyMatchPortMin_Type(InetPortNumber):defaultValue=0
_BsifnPolicyMatchPortMin_Type.__name__=_E
_BsifnPolicyMatchPortMin_Object=MibTableColumn
bsifnPolicyMatchPortMin=_BsifnPolicyMatchPortMin_Object((1,3,6,1,4,1,45,5,35,1,2,1,5),_BsifnPolicyMatchPortMin_Type())
bsifnPolicyMatchPortMin.setMaxAccess(_B)
if mibBuilder.loadTexts:bsifnPolicyMatchPortMin.setStatus(_A)
class _BsifnPolicyMatchPortMax_Type(InetPortNumber):defaultValue=65535
_BsifnPolicyMatchPortMax_Type.__name__=_E
_BsifnPolicyMatchPortMax_Object=MibTableColumn
bsifnPolicyMatchPortMax=_BsifnPolicyMatchPortMax_Object((1,3,6,1,4,1,45,5,35,1,2,1,6),_BsifnPolicyMatchPortMax_Type())
bsifnPolicyMatchPortMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bsifnPolicyMatchPortMax.setStatus(_A)
_BsifnPolicySetNextHopInetAddressType_Type=InetAddressType
_BsifnPolicySetNextHopInetAddressType_Object=MibTableColumn
bsifnPolicySetNextHopInetAddressType=_BsifnPolicySetNextHopInetAddressType_Object((1,3,6,1,4,1,45,5,35,1,2,1,7),_BsifnPolicySetNextHopInetAddressType_Type())
bsifnPolicySetNextHopInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:bsifnPolicySetNextHopInetAddressType.setStatus(_A)
_BsifnPolicySetNextHopInetAddress_Type=InetAddress
_BsifnPolicySetNextHopInetAddress_Object=MibTableColumn
bsifnPolicySetNextHopInetAddress=_BsifnPolicySetNextHopInetAddress_Object((1,3,6,1,4,1,45,5,35,1,2,1,8),_BsifnPolicySetNextHopInetAddress_Type())
bsifnPolicySetNextHopInetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:bsifnPolicySetNextHopInetAddress.setStatus(_A)
_BsifnPolicyRowStatus_Type=RowStatus
_BsifnPolicyRowStatus_Object=MibTableColumn
bsifnPolicyRowStatus=_BsifnPolicyRowStatus_Object((1,3,6,1,4,1,45,5,35,1,2,1,9),_BsifnPolicyRowStatus_Type())
bsifnPolicyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:bsifnPolicyRowStatus.setStatus(_A)
class _BsifnPolicyMatchPortType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tcp',1),('udp',2),('bothTcpAndUdp',3)))
_BsifnPolicyMatchPortType_Type.__name__=_C
_BsifnPolicyMatchPortType_Object=MibTableColumn
bsifnPolicyMatchPortType=_BsifnPolicyMatchPortType_Object((1,3,6,1,4,1,45,5,35,1,2,1,10),_BsifnPolicyMatchPortType_Type())
bsifnPolicyMatchPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:bsifnPolicyMatchPortType.setStatus(_A)
class _BsifnPolicySetSecondNextHopInetAddressType_Type(InetAddressType):defaultValue=1
_BsifnPolicySetSecondNextHopInetAddressType_Type.__name__=_J
_BsifnPolicySetSecondNextHopInetAddressType_Object=MibTableColumn
bsifnPolicySetSecondNextHopInetAddressType=_BsifnPolicySetSecondNextHopInetAddressType_Object((1,3,6,1,4,1,45,5,35,1,2,1,11),_BsifnPolicySetSecondNextHopInetAddressType_Type())
bsifnPolicySetSecondNextHopInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:bsifnPolicySetSecondNextHopInetAddressType.setStatus(_A)
class _BsifnPolicySetSecondNextHopInetAddress_Type(InetAddress):defaultHexValue='00000000'
_BsifnPolicySetSecondNextHopInetAddress_Type.__name__=_I
_BsifnPolicySetSecondNextHopInetAddress_Object=MibTableColumn
bsifnPolicySetSecondNextHopInetAddress=_BsifnPolicySetSecondNextHopInetAddress_Object((1,3,6,1,4,1,45,5,35,1,2,1,12),_BsifnPolicySetSecondNextHopInetAddress_Type())
bsifnPolicySetSecondNextHopInetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:bsifnPolicySetSecondNextHopInetAddress.setStatus(_A)
_BsifnPolicyInterfaceTable_Object=MibTable
bsifnPolicyInterfaceTable=_BsifnPolicyInterfaceTable_Object((1,3,6,1,4,1,45,5,35,1,3))
if mibBuilder.loadTexts:bsifnPolicyInterfaceTable.setStatus(_A)
_BsifnPolicyInterfaceEntry_Object=MibTableRow
bsifnPolicyInterfaceEntry=_BsifnPolicyInterfaceEntry_Object((1,3,6,1,4,1,45,5,35,1,3,1))
bsifnPolicyInterfaceEntry.setIndexNames((0,_D,_L),(1,_D,_M))
if mibBuilder.loadTexts:bsifnPolicyInterfaceEntry.setStatus(_A)
_BsifnPolicyInterfaceIndex_Type=InterfaceIndex
_BsifnPolicyInterfaceIndex_Object=MibTableColumn
bsifnPolicyInterfaceIndex=_BsifnPolicyInterfaceIndex_Object((1,3,6,1,4,1,45,5,35,1,3,1,1),_BsifnPolicyInterfaceIndex_Type())
bsifnPolicyInterfaceIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:bsifnPolicyInterfaceIndex.setStatus(_A)
class _BsifnPolicyInterfacePolicyName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_BsifnPolicyInterfacePolicyName_Type.__name__=_F
_BsifnPolicyInterfacePolicyName_Object=MibTableColumn
bsifnPolicyInterfacePolicyName=_BsifnPolicyInterfacePolicyName_Object((1,3,6,1,4,1,45,5,35,1,3,1,2),_BsifnPolicyInterfacePolicyName_Type())
bsifnPolicyInterfacePolicyName.setMaxAccess(_H)
if mibBuilder.loadTexts:bsifnPolicyInterfacePolicyName.setStatus(_A)
class _BsifnPolicyInterfaceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('drop',1),(_N,2)))
_BsifnPolicyInterfaceMode_Type.__name__=_C
_BsifnPolicyInterfaceMode_Object=MibTableColumn
bsifnPolicyInterfaceMode=_BsifnPolicyInterfaceMode_Object((1,3,6,1,4,1,45,5,35,1,3,1,3),_BsifnPolicyInterfaceMode_Type())
bsifnPolicyInterfaceMode.setMaxAccess(_B)
if mibBuilder.loadTexts:bsifnPolicyInterfaceMode.setStatus(_A)
class _BsifnPolicyInterfaceOperationalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_BsifnPolicyInterfaceOperationalStatus_Type.__name__=_C
_BsifnPolicyInterfaceOperationalStatus_Object=MibTableColumn
bsifnPolicyInterfaceOperationalStatus=_BsifnPolicyInterfaceOperationalStatus_Object((1,3,6,1,4,1,45,5,35,1,3,1,4),_BsifnPolicyInterfaceOperationalStatus_Type())
bsifnPolicyInterfaceOperationalStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:bsifnPolicyInterfaceOperationalStatus.setStatus(_A)
class _BsifnPolicyInterfaceAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('drop',1),(_N,2),('enable',3),('notApplicable',4)))
_BsifnPolicyInterfaceAction_Type.__name__=_C
_BsifnPolicyInterfaceAction_Object=MibTableColumn
bsifnPolicyInterfaceAction=_BsifnPolicyInterfaceAction_Object((1,3,6,1,4,1,45,5,35,1,3,1,5),_BsifnPolicyInterfaceAction_Type())
bsifnPolicyInterfaceAction.setMaxAccess(_G)
if mibBuilder.loadTexts:bsifnPolicyInterfaceAction.setStatus(_A)
_BsifnPolicyInterfaceRowStatus_Type=RowStatus
_BsifnPolicyInterfaceRowStatus_Object=MibTableColumn
bsifnPolicyInterfaceRowStatus=_BsifnPolicyInterfaceRowStatus_Object((1,3,6,1,4,1,45,5,35,1,3,1,6),_BsifnPolicyInterfaceRowStatus_Type())
bsifnPolicyInterfaceRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:bsifnPolicyInterfaceRowStatus.setStatus(_A)
class _BsifnPolicyInterfaceAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_BsifnPolicyInterfaceAdminStatus_Type.__name__=_C
_BsifnPolicyInterfaceAdminStatus_Object=MibTableColumn
bsifnPolicyInterfaceAdminStatus=_BsifnPolicyInterfaceAdminStatus_Object((1,3,6,1,4,1,45,5,35,1,3,1,7),_BsifnPolicyInterfaceAdminStatus_Type())
bsifnPolicyInterfaceAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:bsifnPolicyInterfaceAdminStatus.setStatus(_A)
bsifnInstallationFailure=NotificationType((1,3,6,1,4,1,45,5,35,0,1))
if mibBuilder.loadTexts:bsifnInstallationFailure.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'bayStackIpFwdNhMib':bayStackIpFwdNhMib,'bayStackIpFwdNhNotifications':bayStackIpFwdNhNotifications,'bsifnInstallationFailure':bsifnInstallationFailure,'bayStackIpFwdNhObjects':bayStackIpFwdNhObjects,'bsifnScalars':bsifnScalars,'bsifnIpForwardingNextHopAdminEnabled':bsifnIpForwardingNextHopAdminEnabled,'bsifnIpForwardingNextHopOperEnabled':bsifnIpForwardingNextHopOperEnabled,'bsifnPolicyTable':bsifnPolicyTable,'bsifnPolicyEntry':bsifnPolicyEntry,_K:bsifnPolicyName,'bsifnPolicyMatchInetAddressType':bsifnPolicyMatchInetAddressType,'bsifnPolicyMatchInetAddress':bsifnPolicyMatchInetAddress,'bsifnPolicyMatchInetAddressMask':bsifnPolicyMatchInetAddressMask,'bsifnPolicyMatchPortMin':bsifnPolicyMatchPortMin,'bsifnPolicyMatchPortMax':bsifnPolicyMatchPortMax,'bsifnPolicySetNextHopInetAddressType':bsifnPolicySetNextHopInetAddressType,'bsifnPolicySetNextHopInetAddress':bsifnPolicySetNextHopInetAddress,'bsifnPolicyRowStatus':bsifnPolicyRowStatus,'bsifnPolicyMatchPortType':bsifnPolicyMatchPortType,'bsifnPolicySetSecondNextHopInetAddressType':bsifnPolicySetSecondNextHopInetAddressType,'bsifnPolicySetSecondNextHopInetAddress':bsifnPolicySetSecondNextHopInetAddress,'bsifnPolicyInterfaceTable':bsifnPolicyInterfaceTable,'bsifnPolicyInterfaceEntry':bsifnPolicyInterfaceEntry,_L:bsifnPolicyInterfaceIndex,_M:bsifnPolicyInterfacePolicyName,'bsifnPolicyInterfaceMode':bsifnPolicyInterfaceMode,'bsifnPolicyInterfaceOperationalStatus':bsifnPolicyInterfaceOperationalStatus,'bsifnPolicyInterfaceAction':bsifnPolicyInterfaceAction,'bsifnPolicyInterfaceRowStatus':bsifnPolicyInterfaceRowStatus,'bsifnPolicyInterfaceAdminStatus':bsifnPolicyInterfaceAdminStatus})