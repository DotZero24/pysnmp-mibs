_M='adGenIpHostConnectIfIndex'
_L='adGenIpHostServiceOrInterface'
_K='DisplayString'
_J='Integer32'
_I='OctetString'
_H='not-accessible'
_G='adGenIpHostEntryIndex'
_F='ifIndex'
_E='IF-MIB'
_D='ADTRAN-GENIPHOST-MIB'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenIpHost,adGenIpHostID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenIpHost','adGenIpHostID')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_E,'InterfaceIndexOrZero',_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','RowStatus','TextualConvention','TruthValue')
adGenIpHostIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,18,1))
if mibBuilder.loadTexts:adGenIpHostIdentity.setRevisions(('2016-01-11 00:00','2012-01-20 00:00','2009-11-02 00:00'))
class AdGenIpHostServiceOrInterface(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,50,51)));namedValues=NamedValues(*(('serviceSIP',1),('serviceMGCP',2),('serviceRFVideo',3),('serviceRADIUS',4),('interfacePseudowire',50),('interfacePacketTiming',51)))
_AdGenIpHostProvisioning_ObjectIdentity=ObjectIdentity
adGenIpHostProvisioning=_AdGenIpHostProvisioning_ObjectIdentity((1,3,6,1,4,1,664,5,70,18,1))
_AdGenIpHostProvErrorTable_Object=MibTable
adGenIpHostProvErrorTable=_AdGenIpHostProvErrorTable_Object((1,3,6,1,4,1,664,5,70,18,1,1))
if mibBuilder.loadTexts:adGenIpHostProvErrorTable.setStatus(_A)
_AdGenIpHostProvErrorEntry_Object=MibTableRow
adGenIpHostProvErrorEntry=_AdGenIpHostProvErrorEntry_Object((1,3,6,1,4,1,664,5,70,18,1,1,1))
adGenIpHostProvErrorEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adGenIpHostProvErrorEntry.setStatus(_A)
_AdGenIpHostProvCurrentNumber_Type=Integer32
_AdGenIpHostProvCurrentNumber_Object=MibTableColumn
adGenIpHostProvCurrentNumber=_AdGenIpHostProvCurrentNumber_Object((1,3,6,1,4,1,664,5,70,18,1,1,1,1),_AdGenIpHostProvCurrentNumber_Type())
adGenIpHostProvCurrentNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenIpHostProvCurrentNumber.setStatus(_A)
_AdGenIpHostProvLastCreateError_Type=DisplayString
_AdGenIpHostProvLastCreateError_Object=MibTableColumn
adGenIpHostProvLastCreateError=_AdGenIpHostProvLastCreateError_Object((1,3,6,1,4,1,664,5,70,18,1,1,1,2),_AdGenIpHostProvLastCreateError_Type())
adGenIpHostProvLastCreateError.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenIpHostProvLastCreateError.setStatus(_A)
_AdGenIpHostProvTable_Object=MibTable
adGenIpHostProvTable=_AdGenIpHostProvTable_Object((1,3,6,1,4,1,664,5,70,18,1,2))
if mibBuilder.loadTexts:adGenIpHostProvTable.setStatus(_A)
_AdGenIpHostProvEntry_Object=MibTableRow
adGenIpHostProvEntry=_AdGenIpHostProvEntry_Object((1,3,6,1,4,1,664,5,70,18,1,2,1))
adGenIpHostProvEntry.setIndexNames((0,_E,_F),(1,_D,_G))
if mibBuilder.loadTexts:adGenIpHostProvEntry.setStatus(_A)
class _AdGenIpHostEntryIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_AdGenIpHostEntryIndex_Type.__name__=_K
_AdGenIpHostEntryIndex_Object=MibTableColumn
adGenIpHostEntryIndex=_AdGenIpHostEntryIndex_Object((1,3,6,1,4,1,664,5,70,18,1,2,1,1),_AdGenIpHostEntryIndex_Type())
adGenIpHostEntryIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenIpHostEntryIndex.setStatus(_A)
_AdGenIpHostProvRowStatus_Type=RowStatus
_AdGenIpHostProvRowStatus_Object=MibTableColumn
adGenIpHostProvRowStatus=_AdGenIpHostProvRowStatus_Object((1,3,6,1,4,1,664,5,70,18,1,2,1,2),_AdGenIpHostProvRowStatus_Type())
adGenIpHostProvRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIpHostProvRowStatus.setStatus(_A)
_AdGenIpHostProvLastErrorString_Type=DisplayString
_AdGenIpHostProvLastErrorString_Object=MibTableColumn
adGenIpHostProvLastErrorString=_AdGenIpHostProvLastErrorString_Object((1,3,6,1,4,1,664,5,70,18,1,2,1,3),_AdGenIpHostProvLastErrorString_Type())
adGenIpHostProvLastErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenIpHostProvLastErrorString.setStatus(_A)
_AdGenIpHostProvStatus_Type=DisplayString
_AdGenIpHostProvStatus_Object=MibTableColumn
adGenIpHostProvStatus=_AdGenIpHostProvStatus_Object((1,3,6,1,4,1,664,5,70,18,1,2,1,4),_AdGenIpHostProvStatus_Type())
adGenIpHostProvStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenIpHostProvStatus.setStatus(_A)
_AdGenIpHostSubInterfaceIndex_Type=Integer32
_AdGenIpHostSubInterfaceIndex_Object=MibTableColumn
adGenIpHostSubInterfaceIndex=_AdGenIpHostSubInterfaceIndex_Object((1,3,6,1,4,1,664,5,70,18,1,2,1,5),_AdGenIpHostSubInterfaceIndex_Type())
adGenIpHostSubInterfaceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenIpHostSubInterfaceIndex.setStatus(_A)
_AdGenIpHostProvIpAddress_Type=IpAddress
_AdGenIpHostProvIpAddress_Object=MibTableColumn
adGenIpHostProvIpAddress=_AdGenIpHostProvIpAddress_Object((1,3,6,1,4,1,664,5,70,18,1,2,1,6),_AdGenIpHostProvIpAddress_Type())
adGenIpHostProvIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIpHostProvIpAddress.setStatus(_A)
_AdGenIpHostProvIpSubnetMask_Type=IpAddress
_AdGenIpHostProvIpSubnetMask_Object=MibTableColumn
adGenIpHostProvIpSubnetMask=_AdGenIpHostProvIpSubnetMask_Object((1,3,6,1,4,1,664,5,70,18,1,2,1,7),_AdGenIpHostProvIpSubnetMask_Type())
adGenIpHostProvIpSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIpHostProvIpSubnetMask.setStatus(_A)
_AdGenIpHostProvIpDefaultGateway_Type=IpAddress
_AdGenIpHostProvIpDefaultGateway_Object=MibTableColumn
adGenIpHostProvIpDefaultGateway=_AdGenIpHostProvIpDefaultGateway_Object((1,3,6,1,4,1,664,5,70,18,1,2,1,8),_AdGenIpHostProvIpDefaultGateway_Type())
adGenIpHostProvIpDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIpHostProvIpDefaultGateway.setStatus(_A)
_AdGenIpHostProvDomainName_Type=DisplayString
_AdGenIpHostProvDomainName_Object=MibTableColumn
adGenIpHostProvDomainName=_AdGenIpHostProvDomainName_Object((1,3,6,1,4,1,664,5,70,18,1,2,1,9),_AdGenIpHostProvDomainName_Type())
adGenIpHostProvDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIpHostProvDomainName.setStatus(_A)
_AdGenIpHostProvDomainNameAddServer_Type=IpAddress
_AdGenIpHostProvDomainNameAddServer_Object=MibTableColumn
adGenIpHostProvDomainNameAddServer=_AdGenIpHostProvDomainNameAddServer_Object((1,3,6,1,4,1,664,5,70,18,1,2,1,10),_AdGenIpHostProvDomainNameAddServer_Type())
adGenIpHostProvDomainNameAddServer.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIpHostProvDomainNameAddServer.setStatus(_A)
_AdGenIpHostProvDomainNameRemoveServer_Type=IpAddress
_AdGenIpHostProvDomainNameRemoveServer_Object=MibTableColumn
adGenIpHostProvDomainNameRemoveServer=_AdGenIpHostProvDomainNameRemoveServer_Object((1,3,6,1,4,1,664,5,70,18,1,2,1,11),_AdGenIpHostProvDomainNameRemoveServer_Type())
adGenIpHostProvDomainNameRemoveServer.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIpHostProvDomainNameRemoveServer.setStatus(_A)
class _AdGenIpHostProvDomainNameServerList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(24,24));fixedLength=24
_AdGenIpHostProvDomainNameServerList_Type.__name__=_I
_AdGenIpHostProvDomainNameServerList_Object=MibTableColumn
adGenIpHostProvDomainNameServerList=_AdGenIpHostProvDomainNameServerList_Object((1,3,6,1,4,1,664,5,70,18,1,2,1,12),_AdGenIpHostProvDomainNameServerList_Type())
adGenIpHostProvDomainNameServerList.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIpHostProvDomainNameServerList.setStatus(_A)
_AdGenIpHostProvDomainLookup_Type=TruthValue
_AdGenIpHostProvDomainLookup_Object=MibTableColumn
adGenIpHostProvDomainLookup=_AdGenIpHostProvDomainLookup_Object((1,3,6,1,4,1,664,5,70,18,1,2,1,13),_AdGenIpHostProvDomainLookup_Type())
adGenIpHostProvDomainLookup.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIpHostProvDomainLookup.setStatus(_A)
class _AdGenIpHostProvIpAssignMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dynamic',1),('static',2)))
_AdGenIpHostProvIpAssignMode_Type.__name__=_J
_AdGenIpHostProvIpAssignMode_Object=MibTableColumn
adGenIpHostProvIpAssignMode=_AdGenIpHostProvIpAssignMode_Object((1,3,6,1,4,1,664,5,70,18,1,2,1,14),_AdGenIpHostProvIpAssignMode_Type())
adGenIpHostProvIpAssignMode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIpHostProvIpAssignMode.setStatus(_A)
_AdGenIpHostConnectLastErrorString_Type=DisplayString
_AdGenIpHostConnectLastErrorString_Object=MibTableColumn
adGenIpHostConnectLastErrorString=_AdGenIpHostConnectLastErrorString_Object((1,3,6,1,4,1,664,5,70,18,1,2,1,15),_AdGenIpHostConnectLastErrorString_Type())
adGenIpHostConnectLastErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenIpHostConnectLastErrorString.setStatus(_A)
_AdGenIpHostStatus_ObjectIdentity=ObjectIdentity
adGenIpHostStatus=_AdGenIpHostStatus_ObjectIdentity((1,3,6,1,4,1,664,5,70,18,2))
_AdGenIpHostStatTable_Object=MibTable
adGenIpHostStatTable=_AdGenIpHostStatTable_Object((1,3,6,1,4,1,664,5,70,18,2,1))
if mibBuilder.loadTexts:adGenIpHostStatTable.setStatus(_A)
_AdGenIpHostStatEntry_Object=MibTableRow
adGenIpHostStatEntry=_AdGenIpHostStatEntry_Object((1,3,6,1,4,1,664,5,70,18,2,1,1))
adGenIpHostStatEntry.setIndexNames((0,_E,_F),(1,_D,_G))
if mibBuilder.loadTexts:adGenIpHostStatEntry.setStatus(_A)
_AdGenIpHostStatIpAddress_Type=IpAddress
_AdGenIpHostStatIpAddress_Object=MibTableColumn
adGenIpHostStatIpAddress=_AdGenIpHostStatIpAddress_Object((1,3,6,1,4,1,664,5,70,18,2,1,1,1),_AdGenIpHostStatIpAddress_Type())
adGenIpHostStatIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenIpHostStatIpAddress.setStatus(_A)
_AdGenIpHostStatGateway_Type=IpAddress
_AdGenIpHostStatGateway_Object=MibTableColumn
adGenIpHostStatGateway=_AdGenIpHostStatGateway_Object((1,3,6,1,4,1,664,5,70,18,2,1,1,2),_AdGenIpHostStatGateway_Type())
adGenIpHostStatGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenIpHostStatGateway.setStatus(_A)
_AdGenIpHostStatIpSubnetMask_Type=IpAddress
_AdGenIpHostStatIpSubnetMask_Object=MibTableColumn
adGenIpHostStatIpSubnetMask=_AdGenIpHostStatIpSubnetMask_Object((1,3,6,1,4,1,664,5,70,18,2,1,1,3),_AdGenIpHostStatIpSubnetMask_Type())
adGenIpHostStatIpSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenIpHostStatIpSubnetMask.setStatus(_A)
_AdGenIpHostConnect_ObjectIdentity=ObjectIdentity
adGenIpHostConnect=_AdGenIpHostConnect_ObjectIdentity((1,3,6,1,4,1,664,5,70,18,3))
_AdGenIpHostConnectTable_Object=MibTable
adGenIpHostConnectTable=_AdGenIpHostConnectTable_Object((1,3,6,1,4,1,664,5,70,18,3,1))
if mibBuilder.loadTexts:adGenIpHostConnectTable.setStatus(_A)
_AdGenIpHostConnectEntry_Object=MibTableRow
adGenIpHostConnectEntry=_AdGenIpHostConnectEntry_Object((1,3,6,1,4,1,664,5,70,18,3,1,1))
adGenIpHostConnectEntry.setIndexNames((0,_E,_F),(0,_D,_L),(0,_D,_M),(1,_D,_G))
if mibBuilder.loadTexts:adGenIpHostConnectEntry.setStatus(_A)
_AdGenIpHostServiceOrInterface_Type=AdGenIpHostServiceOrInterface
_AdGenIpHostServiceOrInterface_Object=MibTableColumn
adGenIpHostServiceOrInterface=_AdGenIpHostServiceOrInterface_Object((1,3,6,1,4,1,664,5,70,18,3,1,1,1),_AdGenIpHostServiceOrInterface_Type())
adGenIpHostServiceOrInterface.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenIpHostServiceOrInterface.setStatus(_A)
_AdGenIpHostConnectIfIndex_Type=InterfaceIndexOrZero
_AdGenIpHostConnectIfIndex_Object=MibTableColumn
adGenIpHostConnectIfIndex=_AdGenIpHostConnectIfIndex_Object((1,3,6,1,4,1,664,5,70,18,3,1,1,2),_AdGenIpHostConnectIfIndex_Type())
adGenIpHostConnectIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenIpHostConnectIfIndex.setStatus(_A)
_AdGenIpHostConnectRowStatus_Type=RowStatus
_AdGenIpHostConnectRowStatus_Object=MibTableColumn
adGenIpHostConnectRowStatus=_AdGenIpHostConnectRowStatus_Object((1,3,6,1,4,1,664,5,70,18,3,1,1,3),_AdGenIpHostConnectRowStatus_Type())
adGenIpHostConnectRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenIpHostConnectRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'AdGenIpHostServiceOrInterface':AdGenIpHostServiceOrInterface,'adGenIpHostProvisioning':adGenIpHostProvisioning,'adGenIpHostProvErrorTable':adGenIpHostProvErrorTable,'adGenIpHostProvErrorEntry':adGenIpHostProvErrorEntry,'adGenIpHostProvCurrentNumber':adGenIpHostProvCurrentNumber,'adGenIpHostProvLastCreateError':adGenIpHostProvLastCreateError,'adGenIpHostProvTable':adGenIpHostProvTable,'adGenIpHostProvEntry':adGenIpHostProvEntry,_G:adGenIpHostEntryIndex,'adGenIpHostProvRowStatus':adGenIpHostProvRowStatus,'adGenIpHostProvLastErrorString':adGenIpHostProvLastErrorString,'adGenIpHostProvStatus':adGenIpHostProvStatus,'adGenIpHostSubInterfaceIndex':adGenIpHostSubInterfaceIndex,'adGenIpHostProvIpAddress':adGenIpHostProvIpAddress,'adGenIpHostProvIpSubnetMask':adGenIpHostProvIpSubnetMask,'adGenIpHostProvIpDefaultGateway':adGenIpHostProvIpDefaultGateway,'adGenIpHostProvDomainName':adGenIpHostProvDomainName,'adGenIpHostProvDomainNameAddServer':adGenIpHostProvDomainNameAddServer,'adGenIpHostProvDomainNameRemoveServer':adGenIpHostProvDomainNameRemoveServer,'adGenIpHostProvDomainNameServerList':adGenIpHostProvDomainNameServerList,'adGenIpHostProvDomainLookup':adGenIpHostProvDomainLookup,'adGenIpHostProvIpAssignMode':adGenIpHostProvIpAssignMode,'adGenIpHostConnectLastErrorString':adGenIpHostConnectLastErrorString,'adGenIpHostStatus':adGenIpHostStatus,'adGenIpHostStatTable':adGenIpHostStatTable,'adGenIpHostStatEntry':adGenIpHostStatEntry,'adGenIpHostStatIpAddress':adGenIpHostStatIpAddress,'adGenIpHostStatGateway':adGenIpHostStatGateway,'adGenIpHostStatIpSubnetMask':adGenIpHostStatIpSubnetMask,'adGenIpHostConnect':adGenIpHostConnect,'adGenIpHostConnectTable':adGenIpHostConnectTable,'adGenIpHostConnectEntry':adGenIpHostConnectEntry,_L:adGenIpHostServiceOrInterface,_M:adGenIpHostConnectIfIndex,'adGenIpHostConnectRowStatus':adGenIpHostConnectRowStatus,'adGenIpHostIdentity':adGenIpHostIdentity})