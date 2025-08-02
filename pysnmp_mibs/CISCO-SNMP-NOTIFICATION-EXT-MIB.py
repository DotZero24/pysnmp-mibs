_J='csneNotifyFilterGroup'
_I='csneFilterTimerUnit'
_H='csneFilterAdminTimer'
_G='csneFilterOperTimer'
_F='csneSnmpNotifyFilterEntry'
_E='read-create'
_D='Unsigned32'
_C='Integer32'
_B='CISCO-SNMP-NOTIFICATION-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
snmpNotifyFilterEntry,=mibBuilder.importSymbols('SNMP-NOTIFICATION-MIB','snmpNotifyFilterEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoSnmpNotificationExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,408))
if mibBuilder.loadTexts:ciscoSnmpNotificationExtMIB.setRevisions(('2004-05-12 00:00',))
_CsneMIBNotifs_ObjectIdentity=ObjectIdentity
csneMIBNotifs=_CsneMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,408,0))
_CsneMIBObjects_ObjectIdentity=ObjectIdentity
csneMIBObjects=_CsneMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,408,1))
_CsneNotifyObjects_ObjectIdentity=ObjectIdentity
csneNotifyObjects=_CsneNotifyObjects_ObjectIdentity((1,3,6,1,4,1,9,9,408,1,1))
_CsneSnmpNotifyFilterTable_Object=MibTable
csneSnmpNotifyFilterTable=_CsneSnmpNotifyFilterTable_Object((1,3,6,1,4,1,9,9,408,1,1,1))
if mibBuilder.loadTexts:csneSnmpNotifyFilterTable.setStatus(_A)
_CsneSnmpNotifyFilterEntry_Object=MibTableRow
csneSnmpNotifyFilterEntry=_CsneSnmpNotifyFilterEntry_Object((1,3,6,1,4,1,9,9,408,1,1,1,1))
if mibBuilder.loadTexts:csneSnmpNotifyFilterEntry.setStatus(_A)
class _CsneFilterAdminTimer_Type(Unsigned32):defaultValue=15
_CsneFilterAdminTimer_Type.__name__=_D
_CsneFilterAdminTimer_Object=MibTableColumn
csneFilterAdminTimer=_CsneFilterAdminTimer_Object((1,3,6,1,4,1,9,9,408,1,1,1,1,1),_CsneFilterAdminTimer_Type())
csneFilterAdminTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:csneFilterAdminTimer.setStatus(_A)
_CsneFilterOperTimer_Type=Unsigned32
_CsneFilterOperTimer_Object=MibTableColumn
csneFilterOperTimer=_CsneFilterOperTimer_Object((1,3,6,1,4,1,9,9,408,1,1,1,1,2),_CsneFilterOperTimer_Type())
csneFilterOperTimer.setMaxAccess('read-only')
if mibBuilder.loadTexts:csneFilterOperTimer.setStatus(_A)
class _CsneFilterTimerUnit_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('seconds',1),('minutes',2),('hours',3)))
_CsneFilterTimerUnit_Type.__name__=_C
_CsneFilterTimerUnit_Object=MibTableColumn
csneFilterTimerUnit=_CsneFilterTimerUnit_Object((1,3,6,1,4,1,9,9,408,1,1,1,1,3),_CsneFilterTimerUnit_Type())
csneFilterTimerUnit.setMaxAccess(_E)
if mibBuilder.loadTexts:csneFilterTimerUnit.setStatus(_A)
_CsneMIBConform_ObjectIdentity=ObjectIdentity
csneMIBConform=_CsneMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,408,2))
_CsneMIBCompliances_ObjectIdentity=ObjectIdentity
csneMIBCompliances=_CsneMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,408,2,1))
_CsneMIBGroups_ObjectIdentity=ObjectIdentity
csneMIBGroups=_CsneMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,408,2,2))
snmpNotifyFilterEntry.registerAugmentions((_B,_F))
csneSnmpNotifyFilterEntry.setIndexNames(*snmpNotifyFilterEntry.getIndexNames())
csneNotifyFilterGroup=ObjectGroup((1,3,6,1,4,1,9,9,408,2,2,1))
csneNotifyFilterGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:csneNotifyFilterGroup.setStatus(_A)
csneMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,408,2,1,1))
csneMIBCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:csneMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoSnmpNotificationExtMIB':ciscoSnmpNotificationExtMIB,'csneMIBNotifs':csneMIBNotifs,'csneMIBObjects':csneMIBObjects,'csneNotifyObjects':csneNotifyObjects,'csneSnmpNotifyFilterTable':csneSnmpNotifyFilterTable,_F:csneSnmpNotifyFilterEntry,_H:csneFilterAdminTimer,_G:csneFilterOperTimer,_I:csneFilterTimerUnit,'csneMIBConform':csneMIBConform,'csneMIBCompliances':csneMIBCompliances,'csneMIBCompliance':csneMIBCompliance,'csneMIBGroups':csneMIBGroups,_J:csneNotifyFilterGroup})