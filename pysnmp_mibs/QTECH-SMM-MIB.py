_J='qtechReportSimBillContent'
_I='qtechQuerySimBillContent'
_H='accessible-for-notify'
_G='read-only'
_F='qtechSimImsi'
_E='read-write'
_D='DisplayString'
_C='QTECH-SMM-MIB'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TimeStamp')
qtechSmmMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,120))
if mibBuilder.loadTexts:qtechSmmMIB.setRevisions(('2012-12-10 00:00',))
_QtechSmmObjects_ObjectIdentity=ObjectIdentity
qtechSmmObjects=_QtechSmmObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,120,1))
_QtechReportSimBillSwitch_Type=Unsigned32
_QtechReportSimBillSwitch_Object=MibScalar
qtechReportSimBillSwitch=_QtechReportSimBillSwitch_Object((1,3,6,1,4,1,27514,1,1,10,2,120,1,1),_QtechReportSimBillSwitch_Type())
qtechReportSimBillSwitch.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechReportSimBillSwitch.setStatus(_A)
class _QtechQuerySimBillCmd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_QtechQuerySimBillCmd_Type.__name__=_B
_QtechQuerySimBillCmd_Object=MibScalar
qtechQuerySimBillCmd=_QtechQuerySimBillCmd_Object((1,3,6,1,4,1,27514,1,1,10,2,120,1,2),_QtechQuerySimBillCmd_Type())
qtechQuerySimBillCmd.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechQuerySimBillCmd.setStatus(_A)
_QtechSmsUseTable_Object=MibTable
qtechSmsUseTable=_QtechSmsUseTable_Object((1,3,6,1,4,1,27514,1,1,10,2,120,1,3))
if mibBuilder.loadTexts:qtechSmsUseTable.setStatus(_A)
_QtechSmsUseEntry_Object=MibTableRow
qtechSmsUseEntry=_QtechSmsUseEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,120,1,3,1))
qtechSmsUseEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:qtechSmsUseEntry.setStatus(_A)
class _QtechSimImsi_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_QtechSimImsi_Type.__name__=_D
_QtechSimImsi_Object=MibTableColumn
qtechSimImsi=_QtechSimImsi_Object((1,3,6,1,4,1,27514,1,1,10,2,120,1,3,1,1),_QtechSimImsi_Type())
qtechSimImsi.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechSimImsi.setStatus(_A)
_QtechSmsUseCnt_Type=Unsigned32
_QtechSmsUseCnt_Object=MibTableColumn
qtechSmsUseCnt=_QtechSmsUseCnt_Object((1,3,6,1,4,1,27514,1,1,10,2,120,1,3,1,2),_QtechSmsUseCnt_Type())
qtechSmsUseCnt.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechSmsUseCnt.setStatus(_A)
_QtechSmmTrapObjects_ObjectIdentity=ObjectIdentity
qtechSmmTrapObjects=_QtechSmmTrapObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,120,2))
_QtechSimBillTrapObjects_ObjectIdentity=ObjectIdentity
qtechSimBillTrapObjects=_QtechSimBillTrapObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,120,2,1))
class _QtechQuerySimBillContent_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_QtechQuerySimBillContent_Type.__name__=_B
_QtechQuerySimBillContent_Object=MibScalar
qtechQuerySimBillContent=_QtechQuerySimBillContent_Object((1,3,6,1,4,1,27514,1,1,10,2,120,2,1,1),_QtechQuerySimBillContent_Type())
qtechQuerySimBillContent.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechQuerySimBillContent.setStatus(_A)
class _QtechReportSimBillContent_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_QtechReportSimBillContent_Type.__name__=_B
_QtechReportSimBillContent_Object=MibScalar
qtechReportSimBillContent=_QtechReportSimBillContent_Object((1,3,6,1,4,1,27514,1,1,10,2,120,2,1,2),_QtechReportSimBillContent_Type())
qtechReportSimBillContent.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechReportSimBillContent.setStatus(_A)
_QtechSmmTraps_ObjectIdentity=ObjectIdentity
qtechSmmTraps=_QtechSmmTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,120,3))
_QtechSimBillNotifications_ObjectIdentity=ObjectIdentity
qtechSimBillNotifications=_QtechSimBillNotifications_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,120,3,1))
qtechQuerySimBill=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,120,3,1,1))
qtechQuerySimBill.setObjects((_C,_I))
if mibBuilder.loadTexts:qtechQuerySimBill.setStatus(_A)
qtechReportSimBill=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,120,3,1,2))
qtechReportSimBill.setObjects((_C,_J))
if mibBuilder.loadTexts:qtechReportSimBill.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'qtechSmmMIB':qtechSmmMIB,'qtechSmmObjects':qtechSmmObjects,'qtechReportSimBillSwitch':qtechReportSimBillSwitch,'qtechQuerySimBillCmd':qtechQuerySimBillCmd,'qtechSmsUseTable':qtechSmsUseTable,'qtechSmsUseEntry':qtechSmsUseEntry,_F:qtechSimImsi,'qtechSmsUseCnt':qtechSmsUseCnt,'qtechSmmTrapObjects':qtechSmmTrapObjects,'qtechSimBillTrapObjects':qtechSimBillTrapObjects,_I:qtechQuerySimBillContent,_J:qtechReportSimBillContent,'qtechSmmTraps':qtechSmmTraps,'qtechSimBillNotifications':qtechSimBillNotifications,'qtechQuerySimBill':qtechQuerySimBill,'qtechReportSimBill':qtechReportSimBill})