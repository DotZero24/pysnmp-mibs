_J='ciscoTempMIBGlobalGroup'
_I='ciscoTempOs'
_H='ciscoTempHyst'
_G='ciscoTempValue'
_F='ciscoTempIndex'
_E='Integer32'
_D='degrees Celsius'
_C='read-only'
_B='CISCO-TEMPERATURE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoTempMIB=ModuleIdentity((1,3,6,1,4,1,9,9,870))
if mibBuilder.loadTexts:ciscoTempMIB.setRevisions(('2020-05-28 00:00',))
_CiscoTempMIBInformation_ObjectIdentity=ObjectIdentity
ciscoTempMIBInformation=_CiscoTempMIBInformation_ObjectIdentity((1,3,6,1,4,1,9,9,870,1))
_CiscoTempTable_Object=MibTable
ciscoTempTable=_CiscoTempTable_Object((1,3,6,1,4,1,9,9,870,1,1))
if mibBuilder.loadTexts:ciscoTempTable.setStatus(_A)
_CiscoTempEntry_Object=MibTableRow
ciscoTempEntry=_CiscoTempEntry_Object((1,3,6,1,4,1,9,9,870,1,1,1))
ciscoTempEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:ciscoTempEntry.setStatus(_A)
class _CiscoTempIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CiscoTempIndex_Type.__name__=_E
_CiscoTempIndex_Object=MibTableColumn
ciscoTempIndex=_CiscoTempIndex_Object((1,3,6,1,4,1,9,9,870,1,1,1,1),_CiscoTempIndex_Type())
ciscoTempIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ciscoTempIndex.setStatus(_A)
_CiscoTempValue_Type=Unsigned32
_CiscoTempValue_Object=MibTableColumn
ciscoTempValue=_CiscoTempValue_Object((1,3,6,1,4,1,9,9,870,1,1,1,2),_CiscoTempValue_Type())
ciscoTempValue.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoTempValue.setStatus(_A)
if mibBuilder.loadTexts:ciscoTempValue.setUnits(_D)
_CiscoTempHyst_Type=Unsigned32
_CiscoTempHyst_Object=MibTableColumn
ciscoTempHyst=_CiscoTempHyst_Object((1,3,6,1,4,1,9,9,870,1,1,1,3),_CiscoTempHyst_Type())
ciscoTempHyst.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoTempHyst.setStatus(_A)
if mibBuilder.loadTexts:ciscoTempHyst.setUnits(_D)
_CiscoTempOs_Type=Unsigned32
_CiscoTempOs_Object=MibTableColumn
ciscoTempOs=_CiscoTempOs_Object((1,3,6,1,4,1,9,9,870,1,1,1,4),_CiscoTempOs_Type())
ciscoTempOs.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoTempOs.setStatus(_A)
if mibBuilder.loadTexts:ciscoTempOs.setUnits(_D)
_CiscoTempMIBConform_ObjectIdentity=ObjectIdentity
ciscoTempMIBConform=_CiscoTempMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,870,2))
_CiscoTempMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoTempMIBCompliances=_CiscoTempMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,870,2,1))
_CiscoTempMIBConformGroups_ObjectIdentity=ObjectIdentity
ciscoTempMIBConformGroups=_CiscoTempMIBConformGroups_ObjectIdentity((1,3,6,1,4,1,9,9,870,2,2))
ciscoTempMIBGlobalGroup=ObjectGroup((1,3,6,1,4,1,9,9,870,2,2,1))
ciscoTempMIBGlobalGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:ciscoTempMIBGlobalGroup.setStatus(_A)
ciscoTempMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,870,2,1,1))
ciscoTempMIBCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:ciscoTempMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoTempMIB':ciscoTempMIB,'ciscoTempMIBInformation':ciscoTempMIBInformation,'ciscoTempTable':ciscoTempTable,'ciscoTempEntry':ciscoTempEntry,_F:ciscoTempIndex,_G:ciscoTempValue,_H:ciscoTempHyst,_I:ciscoTempOs,'ciscoTempMIBConform':ciscoTempMIBConform,'ciscoTempMIBCompliances':ciscoTempMIBCompliances,'ciscoTempMIBCompliance':ciscoTempMIBCompliance,'ciscoTempMIBConformGroups':ciscoTempMIBConformGroups,_J:ciscoTempMIBGlobalGroup})