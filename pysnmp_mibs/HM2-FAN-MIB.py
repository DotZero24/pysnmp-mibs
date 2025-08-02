_J='hm2FanMgmtStatus'
_I='hm2FanModuleMgmtStatus'
_H='accessible-for-notify'
_G='hm2FanMgmtFanId'
_F='read-only'
_E='hm2FanModuleMgmtId'
_D='hm2UnitIndex'
_C='HM2-DEVMGMT-MIB'
_B='HM2-FAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hm2UnitIndex,=mibBuilder.importSymbols(_C,_D)
hm2ConfigurationMibs,=mibBuilder.importSymbols('HM2-TC-MIB','hm2ConfigurationMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hm2FanMgmtMib=ModuleIdentity((1,3,6,1,4,1,248,11,13))
if mibBuilder.loadTexts:hm2FanMgmtMib.setRevisions(('2017-04-26 00:00',))
class Hm2FanModuleStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('not-available',1),('available-and-ok',2),('available-but-failure',3)))
_Hm2FanMgmtMibNotifications_ObjectIdentity=ObjectIdentity
hm2FanMgmtMibNotifications=_Hm2FanMgmtMibNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,13,0))
_Hm2FanMgmtMibObjects_ObjectIdentity=ObjectIdentity
hm2FanMgmtMibObjects=_Hm2FanMgmtMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,13,1))
_Hm2FanMgmtGroup_ObjectIdentity=ObjectIdentity
hm2FanMgmtGroup=_Hm2FanMgmtGroup_ObjectIdentity((1,3,6,1,4,1,248,11,13,1,1))
_Hm2FanMgmtGlobalGroup_ObjectIdentity=ObjectIdentity
hm2FanMgmtGlobalGroup=_Hm2FanMgmtGlobalGroup_ObjectIdentity((1,3,6,1,4,1,248,11,13,1,1,1))
_Hm2FanMgmtMaxSuppModulesPerUnit_Type=Unsigned32
_Hm2FanMgmtMaxSuppModulesPerUnit_Object=MibScalar
hm2FanMgmtMaxSuppModulesPerUnit=_Hm2FanMgmtMaxSuppModulesPerUnit_Object((1,3,6,1,4,1,248,11,13,1,1,1,1),_Hm2FanMgmtMaxSuppModulesPerUnit_Type())
hm2FanMgmtMaxSuppModulesPerUnit.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2FanMgmtMaxSuppModulesPerUnit.setStatus(_A)
_Hm2FanMgmtMaxSuppFanPerModule_Type=Unsigned32
_Hm2FanMgmtMaxSuppFanPerModule_Object=MibScalar
hm2FanMgmtMaxSuppFanPerModule=_Hm2FanMgmtMaxSuppFanPerModule_Object((1,3,6,1,4,1,248,11,13,1,1,1,2),_Hm2FanMgmtMaxSuppFanPerModule_Type())
hm2FanMgmtMaxSuppFanPerModule.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2FanMgmtMaxSuppFanPerModule.setStatus(_A)
_Hm2FanModuleMgmtTable_Object=MibTable
hm2FanModuleMgmtTable=_Hm2FanModuleMgmtTable_Object((1,3,6,1,4,1,248,11,13,1,1,2))
if mibBuilder.loadTexts:hm2FanModuleMgmtTable.setStatus(_A)
_Hm2FanModuleMgmtEntry_Object=MibTableRow
hm2FanModuleMgmtEntry=_Hm2FanModuleMgmtEntry_Object((1,3,6,1,4,1,248,11,13,1,1,2,1))
hm2FanModuleMgmtEntry.setIndexNames((0,_C,_D),(0,_B,_E))
if mibBuilder.loadTexts:hm2FanModuleMgmtEntry.setStatus(_A)
_Hm2FanModuleMgmtId_Type=Unsigned32
_Hm2FanModuleMgmtId_Object=MibTableColumn
hm2FanModuleMgmtId=_Hm2FanModuleMgmtId_Object((1,3,6,1,4,1,248,11,13,1,1,2,1,1),_Hm2FanModuleMgmtId_Type())
hm2FanModuleMgmtId.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2FanModuleMgmtId.setStatus(_A)
_Hm2FanModuleMgmtStatus_Type=Hm2FanModuleStatus
_Hm2FanModuleMgmtStatus_Object=MibTableColumn
hm2FanModuleMgmtStatus=_Hm2FanModuleMgmtStatus_Object((1,3,6,1,4,1,248,11,13,1,1,2,1,2),_Hm2FanModuleMgmtStatus_Type())
hm2FanModuleMgmtStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2FanModuleMgmtStatus.setStatus(_A)
_Hm2FanMgmtTable_Object=MibTable
hm2FanMgmtTable=_Hm2FanMgmtTable_Object((1,3,6,1,4,1,248,11,13,1,1,3))
if mibBuilder.loadTexts:hm2FanMgmtTable.setStatus(_A)
_Hm2FanMgmtEntry_Object=MibTableRow
hm2FanMgmtEntry=_Hm2FanMgmtEntry_Object((1,3,6,1,4,1,248,11,13,1,1,3,1))
hm2FanMgmtEntry.setIndexNames((0,_C,_D),(0,_B,_E),(0,_B,_G))
if mibBuilder.loadTexts:hm2FanMgmtEntry.setStatus(_A)
_Hm2FanMgmtFanId_Type=Unsigned32
_Hm2FanMgmtFanId_Object=MibTableColumn
hm2FanMgmtFanId=_Hm2FanMgmtFanId_Object((1,3,6,1,4,1,248,11,13,1,1,3,1,1),_Hm2FanMgmtFanId_Type())
hm2FanMgmtFanId.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2FanMgmtFanId.setStatus(_A)
_Hm2FanMgmtStatus_Type=Hm2FanModuleStatus
_Hm2FanMgmtStatus_Object=MibTableColumn
hm2FanMgmtStatus=_Hm2FanMgmtStatus_Object((1,3,6,1,4,1,248,11,13,1,1,3,1,2),_Hm2FanMgmtStatus_Type())
hm2FanMgmtStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2FanMgmtStatus.setStatus(_A)
hm2FanMgmtModuleNotification=NotificationType((1,3,6,1,4,1,248,11,13,0,1))
hm2FanMgmtModuleNotification.setObjects(*((_C,_D),(_B,_E),(_B,_I)))
if mibBuilder.loadTexts:hm2FanMgmtModuleNotification.setStatus(_A)
hm2FanMgmtFanNotification=NotificationType((1,3,6,1,4,1,248,11,13,0,2))
hm2FanMgmtFanNotification.setObjects(*((_C,_D),(_B,_E),(_B,_G),(_B,_J)))
if mibBuilder.loadTexts:hm2FanMgmtFanNotification.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Hm2FanModuleStatus':Hm2FanModuleStatus,'hm2FanMgmtMib':hm2FanMgmtMib,'hm2FanMgmtMibNotifications':hm2FanMgmtMibNotifications,'hm2FanMgmtModuleNotification':hm2FanMgmtModuleNotification,'hm2FanMgmtFanNotification':hm2FanMgmtFanNotification,'hm2FanMgmtMibObjects':hm2FanMgmtMibObjects,'hm2FanMgmtGroup':hm2FanMgmtGroup,'hm2FanMgmtGlobalGroup':hm2FanMgmtGlobalGroup,'hm2FanMgmtMaxSuppModulesPerUnit':hm2FanMgmtMaxSuppModulesPerUnit,'hm2FanMgmtMaxSuppFanPerModule':hm2FanMgmtMaxSuppFanPerModule,'hm2FanModuleMgmtTable':hm2FanModuleMgmtTable,'hm2FanModuleMgmtEntry':hm2FanModuleMgmtEntry,_E:hm2FanModuleMgmtId,_I:hm2FanModuleMgmtStatus,'hm2FanMgmtTable':hm2FanMgmtTable,'hm2FanMgmtEntry':hm2FanMgmtEntry,_G:hm2FanMgmtFanId,_J:hm2FanMgmtStatus})