_F='qtechcollisionMIBGroups'
_E='qtechLocIfCollisions'
_D='read-only'
_C='qtechEtherlikeIfIndex'
_B='QTECH-ETHERLIKE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
IfIndex,=mibBuilder.importSymbols('QTECH-TC','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
qtechEtherlikeMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,55))
if mibBuilder.loadTexts:qtechEtherlikeMIB.setRevisions(('2009-09-17 00:00',))
_QtechEtherlikeMIBObjects_ObjectIdentity=ObjectIdentity
qtechEtherlikeMIBObjects=_QtechEtherlikeMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,55,1))
_QtechEtherlikeTable_Object=MibTable
qtechEtherlikeTable=_QtechEtherlikeTable_Object((1,3,6,1,4,1,27514,1,1,10,2,55,1,1))
if mibBuilder.loadTexts:qtechEtherlikeTable.setStatus(_A)
_QtechEtherlikeEntry_Object=MibTableRow
qtechEtherlikeEntry=_QtechEtherlikeEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,55,1,1,1))
qtechEtherlikeEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:qtechEtherlikeEntry.setStatus(_A)
_QtechEtherlikeIfIndex_Type=IfIndex
_QtechEtherlikeIfIndex_Object=MibTableColumn
qtechEtherlikeIfIndex=_QtechEtherlikeIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,55,1,1,1,1),_QtechEtherlikeIfIndex_Type())
qtechEtherlikeIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechEtherlikeIfIndex.setStatus(_A)
_QtechLocIfCollisions_Type=Counter64
_QtechLocIfCollisions_Object=MibTableColumn
qtechLocIfCollisions=_QtechLocIfCollisions_Object((1,3,6,1,4,1,27514,1,1,10,2,55,1,1,1,2),_QtechLocIfCollisions_Type())
qtechLocIfCollisions.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechLocIfCollisions.setStatus(_A)
_QtechEtherlikeMIBConformance_ObjectIdentity=ObjectIdentity
qtechEtherlikeMIBConformance=_QtechEtherlikeMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,55,3))
_QtechEtherlikeMIBCompliances_ObjectIdentity=ObjectIdentity
qtechEtherlikeMIBCompliances=_QtechEtherlikeMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,55,3,1))
_QtechEtherlikeMIBGroups_ObjectIdentity=ObjectIdentity
qtechEtherlikeMIBGroups=_QtechEtherlikeMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,55,3,2))
qtechcollisionMIBGroups=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,55,3,2,1))
qtechcollisionMIBGroups.setObjects(*((_B,_C),(_B,_E)))
if mibBuilder.loadTexts:qtechcollisionMIBGroups.setStatus(_A)
qtechEtherlikeMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,55,3,1,1))
qtechEtherlikeMIBCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:qtechEtherlikeMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechEtherlikeMIB':qtechEtherlikeMIB,'qtechEtherlikeMIBObjects':qtechEtherlikeMIBObjects,'qtechEtherlikeTable':qtechEtherlikeTable,'qtechEtherlikeEntry':qtechEtherlikeEntry,_C:qtechEtherlikeIfIndex,_E:qtechLocIfCollisions,'qtechEtherlikeMIBConformance':qtechEtherlikeMIBConformance,'qtechEtherlikeMIBCompliances':qtechEtherlikeMIBCompliances,'qtechEtherlikeMIBCompliance':qtechEtherlikeMIBCompliance,'qtechEtherlikeMIBGroups':qtechEtherlikeMIBGroups,_F:qtechcollisionMIBGroups})