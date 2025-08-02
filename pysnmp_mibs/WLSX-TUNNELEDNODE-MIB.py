_E='wlsxTunneledNodeMAC'
_D='WLSX-TUNNELEDNODE-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wlsxEnterpriseMibModules,=mibBuilder.importSymbols('ARUBA-MIB','wlsxEnterpriseMibModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,snmpModules=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','snmpModules')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TAddress,TDomain,TextualConvention,TestAndIncr,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','StorageType','TAddress','TDomain','TextualConvention','TestAndIncr','TimeInterval','TruthValue')
wlsxTunneledNodeMIB=ModuleIdentity((1,3,6,1,4,1,14823,2,2,1,17))
if mibBuilder.loadTexts:wlsxTunneledNodeMIB.setRevisions(('2020-08-14 17:45',))
_WlsxTunneledNodeOpGroup_ObjectIdentity=ObjectIdentity
wlsxTunneledNodeOpGroup=_WlsxTunneledNodeOpGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,17,1))
_WlsxTunneledNodeRequestTable_Object=MibTable
wlsxTunneledNodeRequestTable=_WlsxTunneledNodeRequestTable_Object((1,3,6,1,4,1,14823,2,2,1,17,1,1))
if mibBuilder.loadTexts:wlsxTunneledNodeRequestTable.setStatus(_A)
_WlsxTunneledNodeRequestEntry_Object=MibTableRow
wlsxTunneledNodeRequestEntry=_WlsxTunneledNodeRequestEntry_Object((1,3,6,1,4,1,14823,2,2,1,17,1,1,1))
wlsxTunneledNodeRequestEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:wlsxTunneledNodeRequestEntry.setStatus(_A)
_WlsxTunneledNodeMAC_Type=MacAddress
_WlsxTunneledNodeMAC_Object=MibTableColumn
wlsxTunneledNodeMAC=_WlsxTunneledNodeMAC_Object((1,3,6,1,4,1,14823,2,2,1,17,1,1,1,1),_WlsxTunneledNodeMAC_Type())
wlsxTunneledNodeMAC.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:wlsxTunneledNodeMAC.setStatus(_A)
_WlsxTunneledNodeIp_Type=IpAddress
_WlsxTunneledNodeIp_Object=MibTableColumn
wlsxTunneledNodeIp=_WlsxTunneledNodeIp_Object((1,3,6,1,4,1,14823,2,2,1,17,1,1,1,2),_WlsxTunneledNodeIp_Type())
wlsxTunneledNodeIp.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxTunneledNodeIp.setStatus(_A)
_WlsxNumTunnels_Type=Integer32
_WlsxNumTunnels_Object=MibTableColumn
wlsxNumTunnels=_WlsxNumTunnels_Object((1,3,6,1,4,1,14823,2,2,1,17,1,1,1,3),_WlsxNumTunnels_Type())
wlsxNumTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxNumTunnels.setStatus(_A)
class _WlsxTunneledNodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('others',1),('corvina',2)))
_WlsxTunneledNodeType_Type.__name__=_C
_WlsxTunneledNodeType_Object=MibTableColumn
wlsxTunneledNodeType=_WlsxTunneledNodeType_Object((1,3,6,1,4,1,14823,2,2,1,17,1,1,1,4),_WlsxTunneledNodeType_Type())
wlsxTunneledNodeType.setMaxAccess(_B)
if mibBuilder.loadTexts:wlsxTunneledNodeType.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'wlsxTunneledNodeMIB':wlsxTunneledNodeMIB,'wlsxTunneledNodeOpGroup':wlsxTunneledNodeOpGroup,'wlsxTunneledNodeRequestTable':wlsxTunneledNodeRequestTable,'wlsxTunneledNodeRequestEntry':wlsxTunneledNodeRequestEntry,_E:wlsxTunneledNodeMAC,'wlsxTunneledNodeIp':wlsxTunneledNodeIp,'wlsxNumTunnels':wlsxNumTunnels,'wlsxTunneledNodeType':wlsxTunneledNodeType})