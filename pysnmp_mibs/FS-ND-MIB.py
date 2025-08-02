_H='fsNDObjectsGroup'
_G='fsNDTotalActiveStaticNeighbors'
_F='fsNDTotalStaticNeighbors'
_E='fsNDTotalActiveDynamicNeighbors'
_D='fsNDTotalActiveNeighbors'
_C='read-only'
_B='FS-ND-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsNDMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,125))
if mibBuilder.loadTexts:fsNDMIB.setRevisions(('2013-12-30 00:00',))
_FsNDMIBObjects_ObjectIdentity=ObjectIdentity
fsNDMIBObjects=_FsNDMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,125,1))
_FsNDTotalActiveNeighbors_Type=Counter32
_FsNDTotalActiveNeighbors_Object=MibScalar
fsNDTotalActiveNeighbors=_FsNDTotalActiveNeighbors_Object((1,3,6,1,4,1,52642,1,1,10,2,125,1,1),_FsNDTotalActiveNeighbors_Type())
fsNDTotalActiveNeighbors.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNDTotalActiveNeighbors.setStatus(_A)
_FsNDTotalActiveDynamicNeighbors_Type=Counter32
_FsNDTotalActiveDynamicNeighbors_Object=MibScalar
fsNDTotalActiveDynamicNeighbors=_FsNDTotalActiveDynamicNeighbors_Object((1,3,6,1,4,1,52642,1,1,10,2,125,1,2),_FsNDTotalActiveDynamicNeighbors_Type())
fsNDTotalActiveDynamicNeighbors.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNDTotalActiveDynamicNeighbors.setStatus(_A)
_FsNDTotalStaticNeighbors_Type=Counter32
_FsNDTotalStaticNeighbors_Object=MibScalar
fsNDTotalStaticNeighbors=_FsNDTotalStaticNeighbors_Object((1,3,6,1,4,1,52642,1,1,10,2,125,1,3),_FsNDTotalStaticNeighbors_Type())
fsNDTotalStaticNeighbors.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNDTotalStaticNeighbors.setStatus(_A)
_FsNDTotalActiveStaticNeighbors_Type=Counter32
_FsNDTotalActiveStaticNeighbors_Object=MibScalar
fsNDTotalActiveStaticNeighbors=_FsNDTotalActiveStaticNeighbors_Object((1,3,6,1,4,1,52642,1,1,10,2,125,1,4),_FsNDTotalActiveStaticNeighbors_Type())
fsNDTotalActiveStaticNeighbors.setMaxAccess(_C)
if mibBuilder.loadTexts:fsNDTotalActiveStaticNeighbors.setStatus(_A)
_FsNDMIBConformance_ObjectIdentity=ObjectIdentity
fsNDMIBConformance=_FsNDMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,125,2))
_FsNDMIBCompliances_ObjectIdentity=ObjectIdentity
fsNDMIBCompliances=_FsNDMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,125,2,1))
_FsNDMIBGroups_ObjectIdentity=ObjectIdentity
fsNDMIBGroups=_FsNDMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,125,2,2))
fsNDObjectsGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,125,2,2,1))
fsNDObjectsGroup.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:fsNDObjectsGroup.setStatus(_A)
fsNDMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,125,2,1,1))
fsNDMIBCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:fsNDMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsNDMIB':fsNDMIB,'fsNDMIBObjects':fsNDMIBObjects,_D:fsNDTotalActiveNeighbors,_E:fsNDTotalActiveDynamicNeighbors,_F:fsNDTotalStaticNeighbors,_G:fsNDTotalActiveStaticNeighbors,'fsNDMIBConformance':fsNDMIBConformance,'fsNDMIBCompliances':fsNDMIBCompliances,'fsNDMIBCompliance':fsNDMIBCompliance,'fsNDMIBGroups':fsNDMIBGroups,_H:fsNDObjectsGroup})