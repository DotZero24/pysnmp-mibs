_J='ciscoSwitchUsageMIBGroup'
_I='cswitchUsageByIngrsIntfHCOctets'
_H='cswitchUsageByIngrsIntfOctets'
_G='cswitchUsageByIngrsIntfHCPkts'
_F='cswitchUsageByIngrsIntfPkts'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='CISCO-SWITCH-USAGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoSwitchUsageMIB=ModuleIdentity((1,3,6,1,4,1,9,9,201))
if mibBuilder.loadTexts:ciscoSwitchUsageMIB.setRevisions(('2001-05-02 00:00',))
_CiscoSwitchUsageMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSwitchUsageMIBObjects=_CiscoSwitchUsageMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,201,1))
_CiscoSwitchUsageStats_ObjectIdentity=ObjectIdentity
ciscoSwitchUsageStats=_CiscoSwitchUsageStats_ObjectIdentity((1,3,6,1,4,1,9,9,201,1,1))
_CswitchUsageStatTable_Object=MibTable
cswitchUsageStatTable=_CswitchUsageStatTable_Object((1,3,6,1,4,1,9,9,201,1,1,1))
if mibBuilder.loadTexts:cswitchUsageStatTable.setStatus(_A)
_CswitchUsageStatEntry_Object=MibTableRow
cswitchUsageStatEntry=_CswitchUsageStatEntry_Object((1,3,6,1,4,1,9,9,201,1,1,1,1))
cswitchUsageStatEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cswitchUsageStatEntry.setStatus(_A)
_CswitchUsageByIngrsIntfPkts_Type=Counter32
_CswitchUsageByIngrsIntfPkts_Object=MibTableColumn
cswitchUsageByIngrsIntfPkts=_CswitchUsageByIngrsIntfPkts_Object((1,3,6,1,4,1,9,9,201,1,1,1,1,1),_CswitchUsageByIngrsIntfPkts_Type())
cswitchUsageByIngrsIntfPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cswitchUsageByIngrsIntfPkts.setStatus(_A)
_CswitchUsageByIngrsIntfHCPkts_Type=Counter64
_CswitchUsageByIngrsIntfHCPkts_Object=MibTableColumn
cswitchUsageByIngrsIntfHCPkts=_CswitchUsageByIngrsIntfHCPkts_Object((1,3,6,1,4,1,9,9,201,1,1,1,1,2),_CswitchUsageByIngrsIntfHCPkts_Type())
cswitchUsageByIngrsIntfHCPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cswitchUsageByIngrsIntfHCPkts.setStatus(_A)
_CswitchUsageByIngrsIntfOctets_Type=Counter32
_CswitchUsageByIngrsIntfOctets_Object=MibTableColumn
cswitchUsageByIngrsIntfOctets=_CswitchUsageByIngrsIntfOctets_Object((1,3,6,1,4,1,9,9,201,1,1,1,1,3),_CswitchUsageByIngrsIntfOctets_Type())
cswitchUsageByIngrsIntfOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cswitchUsageByIngrsIntfOctets.setStatus(_A)
_CswitchUsageByIngrsIntfHCOctets_Type=Counter64
_CswitchUsageByIngrsIntfHCOctets_Object=MibTableColumn
cswitchUsageByIngrsIntfHCOctets=_CswitchUsageByIngrsIntfHCOctets_Object((1,3,6,1,4,1,9,9,201,1,1,1,1,4),_CswitchUsageByIngrsIntfHCOctets_Type())
cswitchUsageByIngrsIntfHCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cswitchUsageByIngrsIntfHCOctets.setStatus(_A)
_CiscoSwitchUsageMIBNotifyPrefix_ObjectIdentity=ObjectIdentity
ciscoSwitchUsageMIBNotifyPrefix=_CiscoSwitchUsageMIBNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,201,2))
_CiscoSwitchUsageMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoSwitchUsageMIBNotifications=_CiscoSwitchUsageMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,201,2,0))
_CiscoSwitchUsageMIBConformance_ObjectIdentity=ObjectIdentity
ciscoSwitchUsageMIBConformance=_CiscoSwitchUsageMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,201,3))
_CiscoSwitchUsageMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoSwitchUsageMIBCompliances=_CiscoSwitchUsageMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,201,3,1))
_CiscoSwitchUsageMIBGroups_ObjectIdentity=ObjectIdentity
ciscoSwitchUsageMIBGroups=_CiscoSwitchUsageMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,201,3,2))
ciscoSwitchUsageMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,201,3,2,1))
ciscoSwitchUsageMIBGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:ciscoSwitchUsageMIBGroup.setStatus(_A)
ciscoSwitchUsageMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,201,3,1,1))
ciscoSwitchUsageMIBCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:ciscoSwitchUsageMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoSwitchUsageMIB':ciscoSwitchUsageMIB,'ciscoSwitchUsageMIBObjects':ciscoSwitchUsageMIBObjects,'ciscoSwitchUsageStats':ciscoSwitchUsageStats,'cswitchUsageStatTable':cswitchUsageStatTable,'cswitchUsageStatEntry':cswitchUsageStatEntry,_F:cswitchUsageByIngrsIntfPkts,_G:cswitchUsageByIngrsIntfHCPkts,_H:cswitchUsageByIngrsIntfOctets,_I:cswitchUsageByIngrsIntfHCOctets,'ciscoSwitchUsageMIBNotifyPrefix':ciscoSwitchUsageMIBNotifyPrefix,'ciscoSwitchUsageMIBNotifications':ciscoSwitchUsageMIBNotifications,'ciscoSwitchUsageMIBConformance':ciscoSwitchUsageMIBConformance,'ciscoSwitchUsageMIBCompliances':ciscoSwitchUsageMIBCompliances,'ciscoSwitchUsageMIBCompliance':ciscoSwitchUsageMIBCompliance,'ciscoSwitchUsageMIBGroups':ciscoSwitchUsageMIBGroups,_J:ciscoSwitchUsageMIBGroup})