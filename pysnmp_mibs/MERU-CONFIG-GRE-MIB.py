_E='mwGreTableIndex'
_D='MERU-CONFIG-GRE-MIB'
_C='DisplayString'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
mwConfiguration,=mibBuilder.importSymbols('MERU-SMI','mwConfiguration')
MwlOnOffSwitch,MwlProfileOwner=mibBuilder.importSymbols('MERU-TC','MwlOnOffSwitch','MwlProfileOwner')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_C,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp','TruthValue')
mwConfigGRE=ModuleIdentity((1,3,6,1,4,1,15983,1,1,4,15))
_MwGreTable_Object=MibTable
mwGreTable=_MwGreTable_Object((1,3,6,1,4,1,15983,1,1,4,15,1))
if mibBuilder.loadTexts:mwGreTable.setStatus(_A)
_MwGreEntry_Object=MibTableRow
mwGreEntry=_MwGreEntry_Object((1,3,6,1,4,1,15983,1,1,4,15,1,1))
mwGreEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:mwGreEntry.setStatus(_A)
_MwGreTableIndex_Type=Integer32
_MwGreTableIndex_Object=MibTableColumn
mwGreTableIndex=_MwGreTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,15,1,1,1),_MwGreTableIndex_Type())
mwGreTableIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:mwGreTableIndex.setStatus(_A)
class _MwGreName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MwGreName_Type.__name__=_C
_MwGreName_Object=MibTableColumn
mwGreName=_MwGreName_Object((1,3,6,1,4,1,15983,1,1,4,15,1,1,2),_MwGreName_Type())
mwGreName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwGreName.setStatus(_A)
_MwGreInterfaceIndex_Type=Unsigned32
_MwGreInterfaceIndex_Object=MibTableColumn
mwGreInterfaceIndex=_MwGreInterfaceIndex_Object((1,3,6,1,4,1,15983,1,1,4,15,1,1,3),_MwGreInterfaceIndex_Type())
mwGreInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mwGreInterfaceIndex.setStatus(_A)
_MwGreDHCPServerIpAddress_Type=IpAddress
_MwGreDHCPServerIpAddress_Object=MibTableColumn
mwGreDHCPServerIpAddress=_MwGreDHCPServerIpAddress_Object((1,3,6,1,4,1,15983,1,1,4,15,1,1,4),_MwGreDHCPServerIpAddress_Type())
mwGreDHCPServerIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mwGreDHCPServerIpAddress.setStatus(_A)
_MwGreLocalInternalAddress_Type=IpAddress
_MwGreLocalInternalAddress_Object=MibTableColumn
mwGreLocalInternalAddress=_MwGreLocalInternalAddress_Object((1,3,6,1,4,1,15983,1,1,4,15,1,1,5),_MwGreLocalInternalAddress_Type())
mwGreLocalInternalAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mwGreLocalInternalAddress.setStatus(_A)
_MwGreLocalInternalNetmask_Type=IpAddress
_MwGreLocalInternalNetmask_Object=MibTableColumn
mwGreLocalInternalNetmask=_MwGreLocalInternalNetmask_Object((1,3,6,1,4,1,15983,1,1,4,15,1,1,6),_MwGreLocalInternalNetmask_Type())
mwGreLocalInternalNetmask.setMaxAccess(_B)
if mibBuilder.loadTexts:mwGreLocalInternalNetmask.setStatus(_A)
_MwGreRemoteEndpointAddress_Type=IpAddress
_MwGreRemoteEndpointAddress_Object=MibTableColumn
mwGreRemoteEndpointAddress=_MwGreRemoteEndpointAddress_Object((1,3,6,1,4,1,15983,1,1,4,15,1,1,7),_MwGreRemoteEndpointAddress_Type())
mwGreRemoteEndpointAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mwGreRemoteEndpointAddress.setStatus(_A)
_MwGreOverrideDefaultDHCPServer_Type=MwlOnOffSwitch
_MwGreOverrideDefaultDHCPServer_Object=MibTableColumn
mwGreOverrideDefaultDHCPServer=_MwGreOverrideDefaultDHCPServer_Object((1,3,6,1,4,1,15983,1,1,4,15,1,1,8),_MwGreOverrideDefaultDHCPServer_Type())
mwGreOverrideDefaultDHCPServer.setMaxAccess(_B)
if mibBuilder.loadTexts:mwGreOverrideDefaultDHCPServer.setStatus(_A)
_MwGreOwner_Type=MwlProfileOwner
_MwGreOwner_Object=MibTableColumn
mwGreOwner=_MwGreOwner_Object((1,3,6,1,4,1,15983,1,1,4,15,1,1,9),_MwGreOwner_Type())
mwGreOwner.setMaxAccess('read-only')
if mibBuilder.loadTexts:mwGreOwner.setStatus(_A)
_MwGreRowStatus_Type=RowStatus
_MwGreRowStatus_Object=MibTableColumn
mwGreRowStatus=_MwGreRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,15,1,1,17),_MwGreRowStatus_Type())
mwGreRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwGreRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'mwConfigGRE':mwConfigGRE,'mwGreTable':mwGreTable,'mwGreEntry':mwGreEntry,_E:mwGreTableIndex,'mwGreName':mwGreName,'mwGreInterfaceIndex':mwGreInterfaceIndex,'mwGreDHCPServerIpAddress':mwGreDHCPServerIpAddress,'mwGreLocalInternalAddress':mwGreLocalInternalAddress,'mwGreLocalInternalNetmask':mwGreLocalInternalNetmask,'mwGreRemoteEndpointAddress':mwGreRemoteEndpointAddress,'mwGreOverrideDefaultDHCPServer':mwGreOverrideDefaultDHCPServer,'mwGreOwner':mwGreOwner,'mwGreRowStatus':mwGreRowStatus})