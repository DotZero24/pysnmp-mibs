_H='read-only'
_G='vrfVrfName'
_F='OCNOS-VRF-MIB'
_E='Integer32'
_D='vrVrId'
_C='OCNOS-VR-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
ipi,=mibBuilder.importSymbols('OCNOS-IPI-MODULE-MIB','ipi')
vrVrId,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
snmpTraps,=mibBuilder.importSymbols('SNMPv2-MIB','snmpTraps')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention')
vrf=ModuleIdentity((1,3,6,1,4,1,36673,3))
if mibBuilder.loadTexts:vrf.setRevisions(('2018-06-21 00:00',))
_VrfVrfTable_Object=MibTable
vrfVrfTable=_VrfVrfTable_Object((1,3,6,1,4,1,36673,3,1))
if mibBuilder.loadTexts:vrfVrfTable.setStatus(_A)
_VrfVrfEntry_Object=MibTableRow
vrfVrfEntry=_VrfVrfEntry_Object((1,3,6,1,4,1,36673,3,1,1))
vrfVrfEntry.setIndexNames((0,_C,_D),(0,_F,_G))
if mibBuilder.loadTexts:vrfVrfEntry.setStatus(_A)
_VrfVrfName_Type=OctetString
_VrfVrfName_Object=MibTableColumn
vrfVrfName=_VrfVrfName_Object((1,3,6,1,4,1,36673,3,1,1,1),_VrfVrfName_Type())
vrfVrfName.setMaxAccess(_B)
if mibBuilder.loadTexts:vrfVrfName.setStatus(_A)
class _VrfMacVrf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_VrfMacVrf_Type.__name__=_E
_VrfMacVrf_Object=MibTableColumn
vrfMacVrf=_VrfMacVrf_Object((1,3,6,1,4,1,36673,3,1,1,2),_VrfMacVrf_Type())
vrfMacVrf.setMaxAccess(_B)
if mibBuilder.loadTexts:vrfMacVrf.setStatus(_A)
_VrfVrfId_Type=Unsigned32
_VrfVrfId_Object=MibTableColumn
vrfVrfId=_VrfVrfId_Object((1,3,6,1,4,1,36673,3,1,1,3),_VrfVrfId_Type())
vrfVrfId.setMaxAccess(_H)
if mibBuilder.loadTexts:vrfVrfId.setStatus(_A)
_VrfFibId_Type=Unsigned32
_VrfFibId_Object=MibTableColumn
vrfFibId=_VrfFibId_Object((1,3,6,1,4,1,36673,3,1,1,4),_VrfFibId_Type())
vrfFibId.setMaxAccess(_H)
if mibBuilder.loadTexts:vrfFibId.setStatus(_A)
_VrfDescription_Type=OctetString
_VrfDescription_Object=MibTableColumn
vrfDescription=_VrfDescription_Object((1,3,6,1,4,1,36673,3,1,1,5),_VrfDescription_Type())
vrfDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:vrfDescription.setStatus(_A)
_VrfRouterId_Type=IpAddress
_VrfRouterId_Object=MibTableColumn
vrfRouterId=_VrfRouterId_Object((1,3,6,1,4,1,36673,3,1,1,6),_VrfRouterId_Type())
vrfRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:vrfRouterId.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'vrf':vrf,'vrfVrfTable':vrfVrfTable,'vrfVrfEntry':vrfVrfEntry,_G:vrfVrfName,'vrfMacVrf':vrfMacVrf,'vrfVrfId':vrfVrfId,'vrfFibId':vrfFibId,'vrfDescription':vrfDescription,'vrfRouterId':vrfRouterId})