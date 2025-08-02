_G='alaVirtualRouterConfigMIBGroup'
_F='alaVirtualRouterNameRowStatus'
_E='alaVirtualRouterNameIndex'
_D='alaVirtualRouterName'
_C='DisplayString'
_B='ALCATEL-IND1-VIRTUALROUTER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
routingIND1Vrf,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','routingIND1Vrf')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','RowStatus','TextualConvention')
alcatelIND1VirtualRouterMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,15,1))
if mibBuilder.loadTexts:alcatelIND1VirtualRouterMIB.setRevisions(('2008-03-17 00:00',))
_AlcatelIND1VirtualRouterMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1VirtualRouterMIBObjects=_AlcatelIND1VirtualRouterMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,15,1,1))
_AlaVirtualRouterConfig_ObjectIdentity=ObjectIdentity
alaVirtualRouterConfig=_AlaVirtualRouterConfig_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,15,1,1,1))
_AlaVirtualRouterNameTable_Object=MibTable
alaVirtualRouterNameTable=_AlaVirtualRouterNameTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,15,1,1,1,1))
if mibBuilder.loadTexts:alaVirtualRouterNameTable.setStatus(_A)
_AlaVirtualRouterNameEntry_Object=MibTableRow
alaVirtualRouterNameEntry=_AlaVirtualRouterNameEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,15,1,1,1,1,1))
alaVirtualRouterNameEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:alaVirtualRouterNameEntry.setStatus(_A)
class _AlaVirtualRouterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_AlaVirtualRouterName_Type.__name__=_C
_AlaVirtualRouterName_Object=MibTableColumn
alaVirtualRouterName=_AlaVirtualRouterName_Object((1,3,6,1,4,1,6486,800,1,2,1,10,15,1,1,1,1,1,1),_AlaVirtualRouterName_Type())
alaVirtualRouterName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:alaVirtualRouterName.setStatus(_A)
_AlaVirtualRouterNameIndex_Type=Unsigned32
_AlaVirtualRouterNameIndex_Object=MibTableColumn
alaVirtualRouterNameIndex=_AlaVirtualRouterNameIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,10,15,1,1,1,1,1,2),_AlaVirtualRouterNameIndex_Type())
alaVirtualRouterNameIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:alaVirtualRouterNameIndex.setStatus(_A)
_AlaVirtualRouterNameRowStatus_Type=RowStatus
_AlaVirtualRouterNameRowStatus_Object=MibTableColumn
alaVirtualRouterNameRowStatus=_AlaVirtualRouterNameRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,15,1,1,1,1,1,3),_AlaVirtualRouterNameRowStatus_Type())
alaVirtualRouterNameRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:alaVirtualRouterNameRowStatus.setStatus(_A)
_AlcatelIND1VirtualRouterMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1VirtualRouterMIBConformance=_AlcatelIND1VirtualRouterMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,15,1,2))
_AlcatelIND1VirtualRouterMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1VirtualRouterMIBCompliances=_AlcatelIND1VirtualRouterMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,15,1,2,1))
_AlcatelIND1VirtualRouterMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1VirtualRouterMIBGroups=_AlcatelIND1VirtualRouterMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,15,1,2,2))
alaVirtualRouterConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,15,1,2,2,1))
alaVirtualRouterConfigMIBGroup.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:alaVirtualRouterConfigMIBGroup.setStatus(_A)
alaVirtualRouterCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,10,15,1,2,1,1))
alaVirtualRouterCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:alaVirtualRouterCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1VirtualRouterMIB':alcatelIND1VirtualRouterMIB,'alcatelIND1VirtualRouterMIBObjects':alcatelIND1VirtualRouterMIBObjects,'alaVirtualRouterConfig':alaVirtualRouterConfig,'alaVirtualRouterNameTable':alaVirtualRouterNameTable,'alaVirtualRouterNameEntry':alaVirtualRouterNameEntry,_D:alaVirtualRouterName,_E:alaVirtualRouterNameIndex,_F:alaVirtualRouterNameRowStatus,'alcatelIND1VirtualRouterMIBConformance':alcatelIND1VirtualRouterMIBConformance,'alcatelIND1VirtualRouterMIBCompliances':alcatelIND1VirtualRouterMIBCompliances,'alaVirtualRouterCompliance':alaVirtualRouterCompliance,'alcatelIND1VirtualRouterMIBGroups':alcatelIND1VirtualRouterMIBGroups,_G:alaVirtualRouterConfigMIBGroup})