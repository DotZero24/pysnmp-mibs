_H='synologyServiceGroup'
_G='serviceUsers'
_F='serviceName'
_E='read-only'
_D='serviceInfoIndex'
_C='Integer32'
_B='SYNOLOGY-SERVICES-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
synologyService=ModuleIdentity((1,3,6,1,4,1,6574,6))
if mibBuilder.loadTexts:synologyService.setRevisions(('2016-05-27 00:00',))
_Synology_ObjectIdentity=ObjectIdentity
synology=_Synology_ObjectIdentity((1,3,6,1,4,1,6574))
_ServiceTable_Object=MibTable
serviceTable=_ServiceTable_Object((1,3,6,1,4,1,6574,6,1))
if mibBuilder.loadTexts:serviceTable.setStatus(_A)
_ServiceEntry_Object=MibTableRow
serviceEntry=_ServiceEntry_Object((1,3,6,1,4,1,6574,6,1,1))
serviceEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:serviceEntry.setStatus(_A)
class _ServiceInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ServiceInfoIndex_Type.__name__=_C
_ServiceInfoIndex_Object=MibTableColumn
serviceInfoIndex=_ServiceInfoIndex_Object((1,3,6,1,4,1,6574,6,1,1,1),_ServiceInfoIndex_Type())
serviceInfoIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:serviceInfoIndex.setStatus(_A)
_ServiceName_Type=OctetString
_ServiceName_Object=MibTableColumn
serviceName=_ServiceName_Object((1,3,6,1,4,1,6574,6,1,1,2),_ServiceName_Type())
serviceName.setMaxAccess(_E)
if mibBuilder.loadTexts:serviceName.setStatus(_A)
_ServiceUsers_Type=Integer32
_ServiceUsers_Object=MibTableColumn
serviceUsers=_ServiceUsers_Object((1,3,6,1,4,1,6574,6,1,1,3),_ServiceUsers_Type())
serviceUsers.setMaxAccess(_E)
if mibBuilder.loadTexts:serviceUsers.setStatus(_A)
_SynologyServiceConformance_ObjectIdentity=ObjectIdentity
synologyServiceConformance=_SynologyServiceConformance_ObjectIdentity((1,3,6,1,4,1,6574,6,2))
_SynologyServiceCompliances_ObjectIdentity=ObjectIdentity
synologyServiceCompliances=_SynologyServiceCompliances_ObjectIdentity((1,3,6,1,4,1,6574,6,2,1))
_SynologyServiceGroups_ObjectIdentity=ObjectIdentity
synologyServiceGroups=_SynologyServiceGroups_ObjectIdentity((1,3,6,1,4,1,6574,6,2,2))
synologyServiceGroup=ObjectGroup((1,3,6,1,4,1,6574,6,2,2,1))
synologyServiceGroup.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:synologyServiceGroup.setStatus(_A)
synologyServiceCompliance=ModuleCompliance((1,3,6,1,4,1,6574,6,2,1,1))
synologyServiceCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:synologyServiceCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'synology':synology,'synologyService':synologyService,'serviceTable':serviceTable,'serviceEntry':serviceEntry,_D:serviceInfoIndex,_F:serviceName,_G:serviceUsers,'synologyServiceConformance':synologyServiceConformance,'synologyServiceCompliances':synologyServiceCompliances,'synologyServiceCompliance':synologyServiceCompliance,'synologyServiceGroups':synologyServiceGroups,_H:synologyServiceGroup})