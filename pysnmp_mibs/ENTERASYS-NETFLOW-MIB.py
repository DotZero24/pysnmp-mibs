_J='etsysNetflowIntfMapGroup'
_I='etsysNetflowExportInterface'
_H='etsysNetflowIfIndex'
_G='read-only'
_F='ifIndex'
_E='IF-MIB'
_D='etsysNetflowExportIntf'
_C='Integer32'
_B='ENTERASYS-NETFLOW-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_E,'InterfaceIndex',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
etsysNetflowMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,61))
if mibBuilder.loadTexts:etsysNetflowMIB.setRevisions(('2007-02-07 19:49','2006-03-22 21:36'))
_EtsysNetflowObjects_ObjectIdentity=ObjectIdentity
etsysNetflowObjects=_EtsysNetflowObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,61,1))
_EtsysNetflowInterfaceMap_ObjectIdentity=ObjectIdentity
etsysNetflowInterfaceMap=_EtsysNetflowInterfaceMap_ObjectIdentity((1,3,6,1,4,1,5624,1,2,61,1,1))
_EtsysNetflowExportIntfMapTable_Object=MibTable
etsysNetflowExportIntfMapTable=_EtsysNetflowExportIntfMapTable_Object((1,3,6,1,4,1,5624,1,2,61,1,1,1))
if mibBuilder.loadTexts:etsysNetflowExportIntfMapTable.setStatus(_A)
_EtsysNetflowExportIntfMapEntry_Object=MibTableRow
etsysNetflowExportIntfMapEntry=_EtsysNetflowExportIntfMapEntry_Object((1,3,6,1,4,1,5624,1,2,61,1,1,1,1))
etsysNetflowExportIntfMapEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:etsysNetflowExportIntfMapEntry.setStatus(_A)
class _EtsysNetflowExportIntf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EtsysNetflowExportIntf_Type.__name__=_C
_EtsysNetflowExportIntf_Object=MibTableColumn
etsysNetflowExportIntf=_EtsysNetflowExportIntf_Object((1,3,6,1,4,1,5624,1,2,61,1,1,1,1,1),_EtsysNetflowExportIntf_Type())
etsysNetflowExportIntf.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:etsysNetflowExportIntf.setStatus(_A)
_EtsysNetflowIfIndex_Type=InterfaceIndex
_EtsysNetflowIfIndex_Object=MibTableColumn
etsysNetflowIfIndex=_EtsysNetflowIfIndex_Object((1,3,6,1,4,1,5624,1,2,61,1,1,1,1,2),_EtsysNetflowIfIndex_Type())
etsysNetflowIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:etsysNetflowIfIndex.setStatus(_A)
_EtsysNetflowIfIndexMapTable_Object=MibTable
etsysNetflowIfIndexMapTable=_EtsysNetflowIfIndexMapTable_Object((1,3,6,1,4,1,5624,1,2,61,1,1,2))
if mibBuilder.loadTexts:etsysNetflowIfIndexMapTable.setStatus(_A)
_EtsysNetflowIfIndexMapEntry_Object=MibTableRow
etsysNetflowIfIndexMapEntry=_EtsysNetflowIfIndexMapEntry_Object((1,3,6,1,4,1,5624,1,2,61,1,1,2,1))
etsysNetflowIfIndexMapEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:etsysNetflowIfIndexMapEntry.setStatus(_A)
class _EtsysNetflowExportInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EtsysNetflowExportInterface_Type.__name__=_C
_EtsysNetflowExportInterface_Object=MibTableColumn
etsysNetflowExportInterface=_EtsysNetflowExportInterface_Object((1,3,6,1,4,1,5624,1,2,61,1,1,2,1,1),_EtsysNetflowExportInterface_Type())
etsysNetflowExportInterface.setMaxAccess(_G)
if mibBuilder.loadTexts:etsysNetflowExportInterface.setStatus(_A)
_EtsysNetflowConformance_ObjectIdentity=ObjectIdentity
etsysNetflowConformance=_EtsysNetflowConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,61,2))
_EtsysNetflowGroups_ObjectIdentity=ObjectIdentity
etsysNetflowGroups=_EtsysNetflowGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,61,2,1))
_EtsysNetflowCompliances_ObjectIdentity=ObjectIdentity
etsysNetflowCompliances=_EtsysNetflowCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,61,2,2))
etsysNetflowIntfMapGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,61,2,1,1))
etsysNetflowIntfMapGroup.setObjects(*((_B,_D),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:etsysNetflowIntfMapGroup.setStatus(_A)
etsysNetflowIntfMapCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,61,2,2,1))
etsysNetflowIntfMapCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:etsysNetflowIntfMapCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysNetflowMIB':etsysNetflowMIB,'etsysNetflowObjects':etsysNetflowObjects,'etsysNetflowInterfaceMap':etsysNetflowInterfaceMap,'etsysNetflowExportIntfMapTable':etsysNetflowExportIntfMapTable,'etsysNetflowExportIntfMapEntry':etsysNetflowExportIntfMapEntry,_D:etsysNetflowExportIntf,_H:etsysNetflowIfIndex,'etsysNetflowIfIndexMapTable':etsysNetflowIfIndexMapTable,'etsysNetflowIfIndexMapEntry':etsysNetflowIfIndexMapEntry,_I:etsysNetflowExportInterface,'etsysNetflowConformance':etsysNetflowConformance,'etsysNetflowGroups':etsysNetflowGroups,_J:etsysNetflowIntfMapGroup,'etsysNetflowCompliances':etsysNetflowCompliances,'etsysNetflowIntfMapCompliance':etsysNetflowIntfMapCompliance})