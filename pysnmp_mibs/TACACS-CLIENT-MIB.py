_H='read-create'
_G='agentTacacsServerIpAddress'
_F='TACACS-CLIENT-MIB'
_E='Integer32'
_D='OctetString'
_C='Unsigned32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fastPath,=mibBuilder.importSymbols('EdgeSwitch-REF-MIB','fastPath')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
agentTacacsClientMIB=ModuleIdentity((1,3,6,1,4,1,4413,1,1,18))
if mibBuilder.loadTexts:agentTacacsClientMIB.setRevisions(('2011-12-14 00:00','2011-01-26 00:00','2007-05-23 00:00','2005-08-17 00:44'))
_AgentTacacsClientObjects_ObjectIdentity=ObjectIdentity
agentTacacsClientObjects=_AgentTacacsClientObjects_ObjectIdentity((1,3,6,1,4,1,4413,1,1,18,1))
_AgentTacacsGlobalConfigGroup_ObjectIdentity=ObjectIdentity
agentTacacsGlobalConfigGroup=_AgentTacacsGlobalConfigGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,18,1,1))
class _AgentTacacsGlobalTimeout_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_AgentTacacsGlobalTimeout_Type.__name__=_C
_AgentTacacsGlobalTimeout_Object=MibScalar
agentTacacsGlobalTimeout=_AgentTacacsGlobalTimeout_Object((1,3,6,1,4,1,4413,1,1,18,1,1,1),_AgentTacacsGlobalTimeout_Type())
agentTacacsGlobalTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:agentTacacsGlobalTimeout.setStatus(_A)
class _AgentTacacsGlobalKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_AgentTacacsGlobalKey_Type.__name__=_D
_AgentTacacsGlobalKey_Object=MibScalar
agentTacacsGlobalKey=_AgentTacacsGlobalKey_Object((1,3,6,1,4,1,4413,1,1,18,1,1,2),_AgentTacacsGlobalKey_Type())
agentTacacsGlobalKey.setMaxAccess(_B)
if mibBuilder.loadTexts:agentTacacsGlobalKey.setStatus(_A)
_AgentTacacsSourceInterface_Type=InterfaceIndexOrZero
_AgentTacacsSourceInterface_Object=MibScalar
agentTacacsSourceInterface=_AgentTacacsSourceInterface_Object((1,3,6,1,4,1,4413,1,1,18,1,1,3),_AgentTacacsSourceInterface_Type())
agentTacacsSourceInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:agentTacacsSourceInterface.setStatus(_A)
class _AgentTacacsServicePortSrcInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('servicePortEnable',1),('servicePortDisable',2)))
_AgentTacacsServicePortSrcInterface_Type.__name__=_E
_AgentTacacsServicePortSrcInterface_Object=MibScalar
agentTacacsServicePortSrcInterface=_AgentTacacsServicePortSrcInterface_Object((1,3,6,1,4,1,4413,1,1,18,1,1,4),_AgentTacacsServicePortSrcInterface_Type())
agentTacacsServicePortSrcInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:agentTacacsServicePortSrcInterface.setStatus(_A)
_AgentTacacsServerTable_Object=MibTable
agentTacacsServerTable=_AgentTacacsServerTable_Object((1,3,6,1,4,1,4413,1,1,18,1,2))
if mibBuilder.loadTexts:agentTacacsServerTable.setStatus(_A)
_AgentTacacsServerEntry_Object=MibTableRow
agentTacacsServerEntry=_AgentTacacsServerEntry_Object((1,3,6,1,4,1,4413,1,1,18,1,2,1))
agentTacacsServerEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:agentTacacsServerEntry.setStatus(_A)
_AgentTacacsServerIpAddress_Type=InetAddress
_AgentTacacsServerIpAddress_Object=MibTableColumn
agentTacacsServerIpAddress=_AgentTacacsServerIpAddress_Object((1,3,6,1,4,1,4413,1,1,18,1,2,1,1),_AgentTacacsServerIpAddress_Type())
agentTacacsServerIpAddress.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:agentTacacsServerIpAddress.setStatus(_A)
class _AgentTacacsPortNumber_Type(Unsigned32):defaultValue=49;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AgentTacacsPortNumber_Type.__name__=_C
_AgentTacacsPortNumber_Object=MibTableColumn
agentTacacsPortNumber=_AgentTacacsPortNumber_Object((1,3,6,1,4,1,4413,1,1,18,1,2,1,2),_AgentTacacsPortNumber_Type())
agentTacacsPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:agentTacacsPortNumber.setStatus(_A)
class _AgentTacacsTimeOut_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_AgentTacacsTimeOut_Type.__name__=_C
_AgentTacacsTimeOut_Object=MibTableColumn
agentTacacsTimeOut=_AgentTacacsTimeOut_Object((1,3,6,1,4,1,4413,1,1,18,1,2,1,3),_AgentTacacsTimeOut_Type())
agentTacacsTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:agentTacacsTimeOut.setStatus(_A)
class _AgentTacacsKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_AgentTacacsKey_Type.__name__=_D
_AgentTacacsKey_Object=MibTableColumn
agentTacacsKey=_AgentTacacsKey_Object((1,3,6,1,4,1,4413,1,1,18,1,2,1,4),_AgentTacacsKey_Type())
agentTacacsKey.setMaxAccess(_B)
if mibBuilder.loadTexts:agentTacacsKey.setStatus(_A)
class _AgentTacacsPriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AgentTacacsPriority_Type.__name__=_C
_AgentTacacsPriority_Object=MibTableColumn
agentTacacsPriority=_AgentTacacsPriority_Object((1,3,6,1,4,1,4413,1,1,18,1,2,1,5),_AgentTacacsPriority_Type())
agentTacacsPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:agentTacacsPriority.setStatus(_A)
_AgentTacacsServerStatus_Type=RowStatus
_AgentTacacsServerStatus_Object=MibTableColumn
agentTacacsServerStatus=_AgentTacacsServerStatus_Object((1,3,6,1,4,1,4413,1,1,18,1,2,1,6),_AgentTacacsServerStatus_Type())
agentTacacsServerStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:agentTacacsServerStatus.setStatus(_A)
_AgentTacacsServerIpAddrType_Type=InetAddressType
_AgentTacacsServerIpAddrType_Object=MibTableColumn
agentTacacsServerIpAddrType=_AgentTacacsServerIpAddrType_Object((1,3,6,1,4,1,4413,1,1,18,1,2,1,7),_AgentTacacsServerIpAddrType_Type())
agentTacacsServerIpAddrType.setMaxAccess(_H)
if mibBuilder.loadTexts:agentTacacsServerIpAddrType.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'agentTacacsClientMIB':agentTacacsClientMIB,'agentTacacsClientObjects':agentTacacsClientObjects,'agentTacacsGlobalConfigGroup':agentTacacsGlobalConfigGroup,'agentTacacsGlobalTimeout':agentTacacsGlobalTimeout,'agentTacacsGlobalKey':agentTacacsGlobalKey,'agentTacacsSourceInterface':agentTacacsSourceInterface,'agentTacacsServicePortSrcInterface':agentTacacsServicePortSrcInterface,'agentTacacsServerTable':agentTacacsServerTable,'agentTacacsServerEntry':agentTacacsServerEntry,_G:agentTacacsServerIpAddress,'agentTacacsPortNumber':agentTacacsPortNumber,'agentTacacsTimeOut':agentTacacsTimeOut,'agentTacacsKey':agentTacacsKey,'agentTacacsPriority':agentTacacsPriority,'agentTacacsServerStatus':agentTacacsServerStatus,'agentTacacsServerIpAddrType':agentTacacsServerIpAddrType})