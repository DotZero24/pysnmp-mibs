_H='qtechNDObjectsGroup'
_G='qtechNDTotalActiveStaticNeighbors'
_F='qtechNDTotalStaticNeighbors'
_E='qtechNDTotalActiveDynamicNeighbors'
_D='qtechNDTotalActiveNeighbors'
_C='read-only'
_B='QTECH-ND-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
qtechNDMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,125))
if mibBuilder.loadTexts:qtechNDMIB.setRevisions(('2013-12-30 00:00',))
_QtechNDMIBObjects_ObjectIdentity=ObjectIdentity
qtechNDMIBObjects=_QtechNDMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,125,1))
_QtechNDTotalActiveNeighbors_Type=Counter32
_QtechNDTotalActiveNeighbors_Object=MibScalar
qtechNDTotalActiveNeighbors=_QtechNDTotalActiveNeighbors_Object((1,3,6,1,4,1,27514,1,1,10,2,125,1,1),_QtechNDTotalActiveNeighbors_Type())
qtechNDTotalActiveNeighbors.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNDTotalActiveNeighbors.setStatus(_A)
_QtechNDTotalActiveDynamicNeighbors_Type=Counter32
_QtechNDTotalActiveDynamicNeighbors_Object=MibScalar
qtechNDTotalActiveDynamicNeighbors=_QtechNDTotalActiveDynamicNeighbors_Object((1,3,6,1,4,1,27514,1,1,10,2,125,1,2),_QtechNDTotalActiveDynamicNeighbors_Type())
qtechNDTotalActiveDynamicNeighbors.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNDTotalActiveDynamicNeighbors.setStatus(_A)
_QtechNDTotalStaticNeighbors_Type=Counter32
_QtechNDTotalStaticNeighbors_Object=MibScalar
qtechNDTotalStaticNeighbors=_QtechNDTotalStaticNeighbors_Object((1,3,6,1,4,1,27514,1,1,10,2,125,1,3),_QtechNDTotalStaticNeighbors_Type())
qtechNDTotalStaticNeighbors.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNDTotalStaticNeighbors.setStatus(_A)
_QtechNDTotalActiveStaticNeighbors_Type=Counter32
_QtechNDTotalActiveStaticNeighbors_Object=MibScalar
qtechNDTotalActiveStaticNeighbors=_QtechNDTotalActiveStaticNeighbors_Object((1,3,6,1,4,1,27514,1,1,10,2,125,1,4),_QtechNDTotalActiveStaticNeighbors_Type())
qtechNDTotalActiveStaticNeighbors.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechNDTotalActiveStaticNeighbors.setStatus(_A)
_QtechNDMIBConformance_ObjectIdentity=ObjectIdentity
qtechNDMIBConformance=_QtechNDMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,125,2))
_QtechNDMIBCompliances_ObjectIdentity=ObjectIdentity
qtechNDMIBCompliances=_QtechNDMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,125,2,1))
_QtechNDMIBGroups_ObjectIdentity=ObjectIdentity
qtechNDMIBGroups=_QtechNDMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,125,2,2))
qtechNDObjectsGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,125,2,2,1))
qtechNDObjectsGroup.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:qtechNDObjectsGroup.setStatus(_A)
qtechNDMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,125,2,1,1))
qtechNDMIBCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:qtechNDMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechNDMIB':qtechNDMIB,'qtechNDMIBObjects':qtechNDMIBObjects,_D:qtechNDTotalActiveNeighbors,_E:qtechNDTotalActiveDynamicNeighbors,_F:qtechNDTotalStaticNeighbors,_G:qtechNDTotalActiveStaticNeighbors,'qtechNDMIBConformance':qtechNDMIBConformance,'qtechNDMIBCompliances':qtechNDMIBCompliances,'qtechNDMIBCompliance':qtechNDMIBCompliance,'qtechNDMIBGroups':qtechNDMIBGroups,_H:qtechNDObjectsGroup})