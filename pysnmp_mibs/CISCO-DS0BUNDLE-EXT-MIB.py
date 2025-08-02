_N='ciscoDs0BundleExtInfoGroup'
_M='ciscoDs0BundleExtConfigGroup'
_L='cdsx0BundleUseDs0Used'
_K='cdsx0BundleExtChannelRate'
_J='cdsx0BundleExtEncapType'
_I='cdsx0BundleExtChannelMap'
_H='cdsx0BundleExtDs1Index'
_G='cdsx0BundleExtEntry'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-write'
_B='CISCO-DS0BUNDLE-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dsx0BundleEntry,=mibBuilder.importSymbols('CISCO-DS0BUNDLE-MIB','dsx0BundleEntry')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_E,'InterfaceIndex',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoDs0BundleExtMIB=ModuleIdentity((1,3,6,1,4,1,9,10,33))
class Ds0ChannelList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_CiscoDs0BundleExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoDs0BundleExtMIBObjects=_CiscoDs0BundleExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,33,1))
_Cdsx0BundleConfig_ObjectIdentity=ObjectIdentity
cdsx0BundleConfig=_Cdsx0BundleConfig_ObjectIdentity((1,3,6,1,4,1,9,10,33,1,1))
_Cdsx0BundleExtTable_Object=MibTable
cdsx0BundleExtTable=_Cdsx0BundleExtTable_Object((1,3,6,1,4,1,9,10,33,1,1,1))
if mibBuilder.loadTexts:cdsx0BundleExtTable.setStatus(_A)
_Cdsx0BundleExtEntry_Object=MibTableRow
cdsx0BundleExtEntry=_Cdsx0BundleExtEntry_Object((1,3,6,1,4,1,9,10,33,1,1,1,1))
if mibBuilder.loadTexts:cdsx0BundleExtEntry.setStatus(_A)
_Cdsx0BundleExtDs1Index_Type=InterfaceIndex
_Cdsx0BundleExtDs1Index_Object=MibTableColumn
cdsx0BundleExtDs1Index=_Cdsx0BundleExtDs1Index_Object((1,3,6,1,4,1,9,10,33,1,1,1,1,1),_Cdsx0BundleExtDs1Index_Type())
cdsx0BundleExtDs1Index.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsx0BundleExtDs1Index.setStatus(_A)
_Cdsx0BundleExtChannelMap_Type=Ds0ChannelList
_Cdsx0BundleExtChannelMap_Object=MibTableColumn
cdsx0BundleExtChannelMap=_Cdsx0BundleExtChannelMap_Object((1,3,6,1,4,1,9,10,33,1,1,1,1,2),_Cdsx0BundleExtChannelMap_Type())
cdsx0BundleExtChannelMap.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsx0BundleExtChannelMap.setStatus(_A)
class _Cdsx0BundleExtEncapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('atmFuni',2),('frameRelay',3)))
_Cdsx0BundleExtEncapType_Type.__name__=_D
_Cdsx0BundleExtEncapType_Object=MibTableColumn
cdsx0BundleExtEncapType=_Cdsx0BundleExtEncapType_Object((1,3,6,1,4,1,9,10,33,1,1,1,1,3),_Cdsx0BundleExtEncapType_Type())
cdsx0BundleExtEncapType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsx0BundleExtEncapType.setStatus(_A)
class _Cdsx0BundleExtChannelRate_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rate56',1),('rate64',2)))
_Cdsx0BundleExtChannelRate_Type.__name__=_D
_Cdsx0BundleExtChannelRate_Object=MibTableColumn
cdsx0BundleExtChannelRate=_Cdsx0BundleExtChannelRate_Object((1,3,6,1,4,1,9,10,33,1,1,1,1,4),_Cdsx0BundleExtChannelRate_Type())
cdsx0BundleExtChannelRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cdsx0BundleExtChannelRate.setStatus(_A)
_Cdsx0BundleInfo_ObjectIdentity=ObjectIdentity
cdsx0BundleInfo=_Cdsx0BundleInfo_ObjectIdentity((1,3,6,1,4,1,9,10,33,1,2))
_Cdsx0BundleUseTable_Object=MibTable
cdsx0BundleUseTable=_Cdsx0BundleUseTable_Object((1,3,6,1,4,1,9,10,33,1,2,1))
if mibBuilder.loadTexts:cdsx0BundleUseTable.setStatus(_A)
_Cdsx0BundleUseEntry_Object=MibTableRow
cdsx0BundleUseEntry=_Cdsx0BundleUseEntry_Object((1,3,6,1,4,1,9,10,33,1,2,1,1))
cdsx0BundleUseEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cdsx0BundleUseEntry.setStatus(_A)
_Cdsx0BundleUseDs0Used_Type=Ds0ChannelList
_Cdsx0BundleUseDs0Used_Object=MibTableColumn
cdsx0BundleUseDs0Used=_Cdsx0BundleUseDs0Used_Object((1,3,6,1,4,1,9,10,33,1,2,1,1,1),_Cdsx0BundleUseDs0Used_Type())
cdsx0BundleUseDs0Used.setMaxAccess('read-only')
if mibBuilder.loadTexts:cdsx0BundleUseDs0Used.setStatus(_A)
_CiscoDs0BundleExtMIBConformance_ObjectIdentity=ObjectIdentity
ciscoDs0BundleExtMIBConformance=_CiscoDs0BundleExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,33,3))
_CiscoDs0BundleExtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoDs0BundleExtMIBCompliances=_CiscoDs0BundleExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,33,3,1))
_CiscoDs0BundleExtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoDs0BundleExtMIBGroups=_CiscoDs0BundleExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,33,3,2))
dsx0BundleEntry.registerAugmentions((_B,_G))
cdsx0BundleExtEntry.setIndexNames(*dsx0BundleEntry.getIndexNames())
ciscoDs0BundleExtConfigGroup=ObjectGroup((1,3,6,1,4,1,9,10,33,3,2,1))
ciscoDs0BundleExtConfigGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:ciscoDs0BundleExtConfigGroup.setStatus(_A)
ciscoDs0BundleExtInfoGroup=ObjectGroup((1,3,6,1,4,1,9,10,33,3,2,2))
ciscoDs0BundleExtInfoGroup.setObjects((_B,_L))
if mibBuilder.loadTexts:ciscoDs0BundleExtInfoGroup.setStatus(_A)
ciscoDs0BundleExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,33,3,1,1))
ciscoDs0BundleExtMIBCompliance.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:ciscoDs0BundleExtMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Ds0ChannelList':Ds0ChannelList,'ciscoDs0BundleExtMIB':ciscoDs0BundleExtMIB,'ciscoDs0BundleExtMIBObjects':ciscoDs0BundleExtMIBObjects,'cdsx0BundleConfig':cdsx0BundleConfig,'cdsx0BundleExtTable':cdsx0BundleExtTable,_G:cdsx0BundleExtEntry,_H:cdsx0BundleExtDs1Index,_I:cdsx0BundleExtChannelMap,_J:cdsx0BundleExtEncapType,_K:cdsx0BundleExtChannelRate,'cdsx0BundleInfo':cdsx0BundleInfo,'cdsx0BundleUseTable':cdsx0BundleUseTable,'cdsx0BundleUseEntry':cdsx0BundleUseEntry,_L:cdsx0BundleUseDs0Used,'ciscoDs0BundleExtMIBConformance':ciscoDs0BundleExtMIBConformance,'ciscoDs0BundleExtMIBCompliances':ciscoDs0BundleExtMIBCompliances,'ciscoDs0BundleExtMIBCompliance':ciscoDs0BundleExtMIBCompliance,'ciscoDs0BundleExtMIBGroups':ciscoDs0BundleExtMIBGroups,_M:ciscoDs0BundleExtConfigGroup,_N:ciscoDs0BundleExtInfoGroup})