_M='ciscoSVITrackedVlanGroup'
_L='ciscoSVIAutostateGroup'
_K='csaTrackedVlansHigh'
_J='csaTrackedVlansLow'
_I='csaInterfaceMode'
_H='csaFeatureEnable'
_G='Integer32'
_F='ifIndex'
_E='IF-MIB'
_D='OctetString'
_C='read-write'
_B='CISCO-SVI-AUTOSTATE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoSVIAutostateMIB=ModuleIdentity((1,3,6,1,4,1,9,9,376))
if mibBuilder.loadTexts:ciscoSVIAutostateMIB.setRevisions(('2004-04-06 00:00',))
_CiscoSVIAutostateMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoSVIAutostateMIBNotifs=_CiscoSVIAutostateMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,376,0))
_CiscoSVIAutostateMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSVIAutostateMIBObjects=_CiscoSVIAutostateMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,376,1))
_CsaGlobal_ObjectIdentity=ObjectIdentity
csaGlobal=_CsaGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,376,1,1))
_CsaFeatureEnable_Type=TruthValue
_CsaFeatureEnable_Object=MibScalar
csaFeatureEnable=_CsaFeatureEnable_Object((1,3,6,1,4,1,9,9,376,1,1,1),_CsaFeatureEnable_Type())
csaFeatureEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:csaFeatureEnable.setStatus(_A)
class _CsaTrackedVlansLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_CsaTrackedVlansLow_Type.__name__=_D
_CsaTrackedVlansLow_Object=MibScalar
csaTrackedVlansLow=_CsaTrackedVlansLow_Object((1,3,6,1,4,1,9,9,376,1,1,2),_CsaTrackedVlansLow_Type())
csaTrackedVlansLow.setMaxAccess(_C)
if mibBuilder.loadTexts:csaTrackedVlansLow.setStatus(_A)
class _CsaTrackedVlansHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_CsaTrackedVlansHigh_Type.__name__=_D
_CsaTrackedVlansHigh_Object=MibScalar
csaTrackedVlansHigh=_CsaTrackedVlansHigh_Object((1,3,6,1,4,1,9,9,376,1,1,3),_CsaTrackedVlansHigh_Type())
csaTrackedVlansHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:csaTrackedVlansHigh.setStatus(_A)
_CsaInterface_ObjectIdentity=ObjectIdentity
csaInterface=_CsaInterface_ObjectIdentity((1,3,6,1,4,1,9,9,376,1,2))
_CsaIfConfigTable_Object=MibTable
csaIfConfigTable=_CsaIfConfigTable_Object((1,3,6,1,4,1,9,9,376,1,2,1))
if mibBuilder.loadTexts:csaIfConfigTable.setStatus(_A)
_CsaIfConfigEntry_Object=MibTableRow
csaIfConfigEntry=_CsaIfConfigEntry_Object((1,3,6,1,4,1,9,9,376,1,2,1,1))
csaIfConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:csaIfConfigEntry.setStatus(_A)
class _CsaInterfaceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('exclude',2),('track',3)))
_CsaInterfaceMode_Type.__name__=_G
_CsaInterfaceMode_Object=MibTableColumn
csaInterfaceMode=_CsaInterfaceMode_Object((1,3,6,1,4,1,9,9,376,1,2,1,1,1),_CsaInterfaceMode_Type())
csaInterfaceMode.setMaxAccess(_C)
if mibBuilder.loadTexts:csaInterfaceMode.setStatus(_A)
_CiscoSVIAutostateMIBConformance_ObjectIdentity=ObjectIdentity
ciscoSVIAutostateMIBConformance=_CiscoSVIAutostateMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,376,2))
_CsaMIBCompliances_ObjectIdentity=ObjectIdentity
csaMIBCompliances=_CsaMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,376,2,1))
_CsaMIBGroups_ObjectIdentity=ObjectIdentity
csaMIBGroups=_CsaMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,376,2,2))
ciscoSVIAutostateGroup=ObjectGroup((1,3,6,1,4,1,9,9,376,2,2,1))
ciscoSVIAutostateGroup.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:ciscoSVIAutostateGroup.setStatus(_A)
ciscoSVITrackedVlanGroup=ObjectGroup((1,3,6,1,4,1,9,9,376,2,2,2))
ciscoSVITrackedVlanGroup.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:ciscoSVITrackedVlanGroup.setStatus(_A)
csaMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,376,2,1,1))
csaMIBCompliance.setObjects(*((_B,_L),(_B,_M)))
if mibBuilder.loadTexts:csaMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoSVIAutostateMIB':ciscoSVIAutostateMIB,'ciscoSVIAutostateMIBNotifs':ciscoSVIAutostateMIBNotifs,'ciscoSVIAutostateMIBObjects':ciscoSVIAutostateMIBObjects,'csaGlobal':csaGlobal,_H:csaFeatureEnable,_J:csaTrackedVlansLow,_K:csaTrackedVlansHigh,'csaInterface':csaInterface,'csaIfConfigTable':csaIfConfigTable,'csaIfConfigEntry':csaIfConfigEntry,_I:csaInterfaceMode,'ciscoSVIAutostateMIBConformance':ciscoSVIAutostateMIBConformance,'csaMIBCompliances':csaMIBCompliances,'csaMIBCompliance':csaMIBCompliance,'csaMIBGroups':csaMIBGroups,_L:ciscoSVIAutostateGroup,_M:ciscoSVITrackedVlanGroup})