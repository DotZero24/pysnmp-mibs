_K='ciscoVlanBridgingMIBGroup2'
_J='ciscoVlanBridgingMIBGroup'
_I='cvbStpForwardingMap2k'
_H='cvbStpForwardingMap'
_G='read-only'
_F='vtpVlanIndex'
_E='CISCO-VTP-MIB'
_D='OctetString'
_C='deprecated'
_B='CISCO-VLAN-BRIDGING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoPortList,=mibBuilder.importSymbols('CISCO-TC','CiscoPortList')
vtpVlanIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoVlanBridgingMIB=ModuleIdentity((1,3,6,1,4,1,9,9,56))
if mibBuilder.loadTexts:ciscoVlanBridgingMIB.setRevisions(('2003-08-22 00:00','1996-09-12 00:00'))
_CiscoVlanBridgingMIBObjects_ObjectIdentity=ObjectIdentity
ciscoVlanBridgingMIBObjects=_CiscoVlanBridgingMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,56,1))
_CvbStp_ObjectIdentity=ObjectIdentity
cvbStp=_CvbStp_ObjectIdentity((1,3,6,1,4,1,9,9,56,1,1))
_CvbStpTable_Object=MibTable
cvbStpTable=_CvbStpTable_Object((1,3,6,1,4,1,9,9,56,1,1,1))
if mibBuilder.loadTexts:cvbStpTable.setStatus(_A)
_CvbStpEntry_Object=MibTableRow
cvbStpEntry=_CvbStpEntry_Object((1,3,6,1,4,1,9,9,56,1,1,1,1))
cvbStpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cvbStpEntry.setStatus(_A)
class _CvbStpForwardingMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CvbStpForwardingMap_Type.__name__=_D
_CvbStpForwardingMap_Object=MibTableColumn
cvbStpForwardingMap=_CvbStpForwardingMap_Object((1,3,6,1,4,1,9,9,56,1,1,1,1,2),_CvbStpForwardingMap_Type())
cvbStpForwardingMap.setMaxAccess(_G)
if mibBuilder.loadTexts:cvbStpForwardingMap.setStatus(_C)
_CvbStpForwardingMap2k_Type=CiscoPortList
_CvbStpForwardingMap2k_Object=MibTableColumn
cvbStpForwardingMap2k=_CvbStpForwardingMap2k_Object((1,3,6,1,4,1,9,9,56,1,1,1,1,3),_CvbStpForwardingMap2k_Type())
cvbStpForwardingMap2k.setMaxAccess(_G)
if mibBuilder.loadTexts:cvbStpForwardingMap2k.setStatus(_A)
_CiscoVlanBridgingMIBConformance_ObjectIdentity=ObjectIdentity
ciscoVlanBridgingMIBConformance=_CiscoVlanBridgingMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,56,3))
_CiscoVlanBridgingMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoVlanBridgingMIBCompliances=_CiscoVlanBridgingMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,56,3,1))
_CiscoVlanBridgingMIBGroups_ObjectIdentity=ObjectIdentity
ciscoVlanBridgingMIBGroups=_CiscoVlanBridgingMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,56,3,2))
ciscoVlanBridgingMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,56,3,2,1))
ciscoVlanBridgingMIBGroup.setObjects((_B,_H))
if mibBuilder.loadTexts:ciscoVlanBridgingMIBGroup.setStatus(_C)
ciscoVlanBridgingMIBGroup2=ObjectGroup((1,3,6,1,4,1,9,9,56,3,2,2))
ciscoVlanBridgingMIBGroup2.setObjects((_B,_I))
if mibBuilder.loadTexts:ciscoVlanBridgingMIBGroup2.setStatus(_A)
ciscoVlanBridgingMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,56,3,1,1))
ciscoVlanBridgingMIBCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:ciscoVlanBridgingMIBCompliance.setStatus(_C)
ciscoVlanBridgingMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,56,3,1,2))
ciscoVlanBridgingMIBCompliance2.setObjects((_B,_K))
if mibBuilder.loadTexts:ciscoVlanBridgingMIBCompliance2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoVlanBridgingMIB':ciscoVlanBridgingMIB,'ciscoVlanBridgingMIBObjects':ciscoVlanBridgingMIBObjects,'cvbStp':cvbStp,'cvbStpTable':cvbStpTable,'cvbStpEntry':cvbStpEntry,_H:cvbStpForwardingMap,_I:cvbStpForwardingMap2k,'ciscoVlanBridgingMIBConformance':ciscoVlanBridgingMIBConformance,'ciscoVlanBridgingMIBCompliances':ciscoVlanBridgingMIBCompliances,'ciscoVlanBridgingMIBCompliance':ciscoVlanBridgingMIBCompliance,'ciscoVlanBridgingMIBCompliance2':ciscoVlanBridgingMIBCompliance2,'ciscoVlanBridgingMIBGroups':ciscoVlanBridgingMIBGroups,_J:ciscoVlanBridgingMIBGroup,_K:ciscoVlanBridgingMIBGroup2})