_P='baud115200'
_O='baud57600'
_N='baud38400'
_M='baud19200'
_L='baud9600'
_K='DisplayString'
_J='enable'
_I='disable'
_H='adGenSlotInfoIndex'
_G='ADTRAN-GENSLOT-MIB'
_F='active'
_E='inactive'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_G,_H)
adShared,=mibBuilder.importSymbols('ADTRAN-MIB','adShared')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','TextualConvention')
adGenESCUmg=ModuleIdentity((1,3,6,1,4,1,664,5,17))
if mibBuilder.loadTexts:adGenESCUmg.setRevisions(('2010-02-24 13:00',))
_AdGenESCUConfig_ObjectIdentity=ObjectIdentity
adGenESCUConfig=_AdGenESCUConfig_ObjectIdentity((1,3,6,1,4,1,664,5,17,1))
_AdGenESCUProv_ObjectIdentity=ObjectIdentity
adGenESCUProv=_AdGenESCUProv_ObjectIdentity((1,3,6,1,4,1,664,5,17,2))
_AdGenESCUProvTable_Object=MibTable
adGenESCUProvTable=_AdGenESCUProvTable_Object((1,3,6,1,4,1,664,5,17,2,1))
if mibBuilder.loadTexts:adGenESCUProvTable.setStatus(_A)
_AdGenESCUProvEntry_Object=MibTableRow
adGenESCUProvEntry=_AdGenESCUProvEntry_Object((1,3,6,1,4,1,664,5,17,2,1,1))
adGenESCUProvEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:adGenESCUProvEntry.setStatus(_A)
class _AdGenESCUadminPortRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5)))
_AdGenESCUadminPortRate_Type.__name__=_B
_AdGenESCUadminPortRate_Object=MibTableColumn
adGenESCUadminPortRate=_AdGenESCUadminPortRate_Object((1,3,6,1,4,1,664,5,17,2,1,1,1),_AdGenESCUadminPortRate_Type())
adGenESCUadminPortRate.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenESCUadminPortRate.setStatus(_A)
class _AdGenESCUautoLogoff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_AdGenESCUautoLogoff_Type.__name__=_B
_AdGenESCUautoLogoff_Object=MibTableColumn
adGenESCUautoLogoff=_AdGenESCUautoLogoff_Object((1,3,6,1,4,1,664,5,17,2,1,1,2),_AdGenESCUautoLogoff_Type())
adGenESCUautoLogoff.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenESCUautoLogoff.setStatus(_A)
class _AdGenESCUautoLogoffTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_AdGenESCUautoLogoffTimer_Type.__name__=_B
_AdGenESCUautoLogoffTimer_Object=MibTableColumn
adGenESCUautoLogoffTimer=_AdGenESCUautoLogoffTimer_Object((1,3,6,1,4,1,664,5,17,2,1,1,3),_AdGenESCUautoLogoffTimer_Type())
adGenESCUautoLogoffTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenESCUautoLogoffTimer.setStatus(_A)
class _AdGenESCUmoduleAutoProv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_AdGenESCUmoduleAutoProv_Type.__name__=_B
_AdGenESCUmoduleAutoProv_Object=MibTableColumn
adGenESCUmoduleAutoProv=_AdGenESCUmoduleAutoProv_Object((1,3,6,1,4,1,664,5,17,2,1,1,4),_AdGenESCUmoduleAutoProv_Type())
adGenESCUmoduleAutoProv.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenESCUmoduleAutoProv.setStatus(_A)
class _AdGenESCUmuxAutoProv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_AdGenESCUmuxAutoProv_Type.__name__=_B
_AdGenESCUmuxAutoProv_Object=MibTableColumn
adGenESCUmuxAutoProv=_AdGenESCUmuxAutoProv_Object((1,3,6,1,4,1,664,5,17,2,1,1,5),_AdGenESCUmuxAutoProv_Type())
adGenESCUmuxAutoProv.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenESCUmuxAutoProv.setStatus(_A)
class _AdGenESCUrestoreFactoryDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('restoreFactoryDefaults',1))
_AdGenESCUrestoreFactoryDefaults_Type.__name__=_B
_AdGenESCUrestoreFactoryDefaults_Object=MibTableColumn
adGenESCUrestoreFactoryDefaults=_AdGenESCUrestoreFactoryDefaults_Object((1,3,6,1,4,1,664,5,17,2,1,1,6),_AdGenESCUrestoreFactoryDefaults_Type())
adGenESCUrestoreFactoryDefaults.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenESCUrestoreFactoryDefaults.setStatus(_A)
class _AdGenESCUadminPortMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('menus',1),('tl1',2)))
_AdGenESCUadminPortMode_Type.__name__=_B
_AdGenESCUadminPortMode_Object=MibTableColumn
adGenESCUadminPortMode=_AdGenESCUadminPortMode_Object((1,3,6,1,4,1,664,5,17,2,1,1,7),_AdGenESCUadminPortMode_Type())
adGenESCUadminPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenESCUadminPortMode.setStatus(_A)
class _AdGenESCUcraftPortRate_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5)))
_AdGenESCUcraftPortRate_Type.__name__=_B
_AdGenESCUcraftPortRate_Object=MibTableColumn
adGenESCUcraftPortRate=_AdGenESCUcraftPortRate_Object((1,3,6,1,4,1,664,5,17,2,1,1,8),_AdGenESCUcraftPortRate_Type())
adGenESCUcraftPortRate.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenESCUcraftPortRate.setStatus(_A)
class _AdGenESCUadminSecurityEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_AdGenESCUadminSecurityEnable_Type.__name__=_B
_AdGenESCUadminSecurityEnable_Object=MibTableColumn
adGenESCUadminSecurityEnable=_AdGenESCUadminSecurityEnable_Object((1,3,6,1,4,1,664,5,17,2,1,1,9),_AdGenESCUadminSecurityEnable_Type())
adGenESCUadminSecurityEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenESCUadminSecurityEnable.setStatus(_A)
_AdGenESCUStatus_ObjectIdentity=ObjectIdentity
adGenESCUStatus=_AdGenESCUStatus_ObjectIdentity((1,3,6,1,4,1,664,5,17,3))
_AdGenESCUStatusTable_Object=MibTable
adGenESCUStatusTable=_AdGenESCUStatusTable_Object((1,3,6,1,4,1,664,5,17,3,1))
if mibBuilder.loadTexts:adGenESCUStatusTable.setStatus(_A)
_AdGenESCUStatusEntry_Object=MibTableRow
adGenESCUStatusEntry=_AdGenESCUStatusEntry_Object((1,3,6,1,4,1,664,5,17,3,1,1))
adGenESCUStatusEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:adGenESCUStatusEntry.setStatus(_A)
class _AdGenESCUacoStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_AdGenESCUacoStatus_Type.__name__=_B
_AdGenESCUacoStatus_Object=MibTableColumn
adGenESCUacoStatus=_AdGenESCUacoStatus_Object((1,3,6,1,4,1,664,5,17,3,1,1,1),_AdGenESCUacoStatus_Type())
adGenESCUacoStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenESCUacoStatus.setStatus(_A)
class _AdGenESCUacoinStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AdGenESCUacoinStatus_Type.__name__=_B
_AdGenESCUacoinStatus_Object=MibTableColumn
adGenESCUacoinStatus=_AdGenESCUacoinStatus_Object((1,3,6,1,4,1,664,5,17,3,1,1,2),_AdGenESCUacoinStatus_Type())
adGenESCUacoinStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenESCUacoinStatus.setStatus(_A)
class _AdGenESCUrmtinStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AdGenESCUrmtinStatus_Type.__name__=_B
_AdGenESCUrmtinStatus_Object=MibTableColumn
adGenESCUrmtinStatus=_AdGenESCUrmtinStatus_Object((1,3,6,1,4,1,664,5,17,3,1,1,3),_AdGenESCUrmtinStatus_Type())
adGenESCUrmtinStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenESCUrmtinStatus.setStatus(_A)
class _AdGenESCUextin1Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AdGenESCUextin1Status_Type.__name__=_B
_AdGenESCUextin1Status_Object=MibTableColumn
adGenESCUextin1Status=_AdGenESCUextin1Status_Object((1,3,6,1,4,1,664,5,17,3,1,1,4),_AdGenESCUextin1Status_Type())
adGenESCUextin1Status.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenESCUextin1Status.setStatus(_A)
class _AdGenESCUextin2Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AdGenESCUextin2Status_Type.__name__=_B
_AdGenESCUextin2Status_Object=MibTableColumn
adGenESCUextin2Status=_AdGenESCUextin2Status_Object((1,3,6,1,4,1,664,5,17,3,1,1,5),_AdGenESCUextin2Status_Type())
adGenESCUextin2Status.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenESCUextin2Status.setStatus(_A)
class _AdGenESCUminus48PowerAStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AdGenESCUminus48PowerAStatus_Type.__name__=_B
_AdGenESCUminus48PowerAStatus_Object=MibTableColumn
adGenESCUminus48PowerAStatus=_AdGenESCUminus48PowerAStatus_Object((1,3,6,1,4,1,664,5,17,3,1,1,6),_AdGenESCUminus48PowerAStatus_Type())
adGenESCUminus48PowerAStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenESCUminus48PowerAStatus.setStatus(_A)
class _AdGenESCUminus48PowerBStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AdGenESCUminus48PowerBStatus_Type.__name__=_B
_AdGenESCUminus48PowerBStatus_Object=MibTableColumn
adGenESCUminus48PowerBStatus=_AdGenESCUminus48PowerBStatus_Object((1,3,6,1,4,1,664,5,17,3,1,1,7),_AdGenESCUminus48PowerBStatus_Type())
adGenESCUminus48PowerBStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenESCUminus48PowerBStatus.setStatus(_A)
class _AdGenESCUopenFuseStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('open',2)))
_AdGenESCUopenFuseStatus_Type.__name__=_B
_AdGenESCUopenFuseStatus_Object=MibTableColumn
adGenESCUopenFuseStatus=_AdGenESCUopenFuseStatus_Object((1,3,6,1,4,1,664,5,17,3,1,1,8),_AdGenESCUopenFuseStatus_Type())
adGenESCUopenFuseStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenESCUopenFuseStatus.setStatus(_A)
class _AdGenESCUCLLI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AdGenESCUCLLI_Type.__name__=_K
_AdGenESCUCLLI_Object=MibTableColumn
adGenESCUCLLI=_AdGenESCUCLLI_Object((1,3,6,1,4,1,664,5,17,3,1,1,9),_AdGenESCUCLLI_Type())
adGenESCUCLLI.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenESCUCLLI.setStatus(_A)
class _AdGenESCUTIRKSID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_AdGenESCUTIRKSID_Type.__name__=_B
_AdGenESCUTIRKSID_Object=MibTableColumn
adGenESCUTIRKSID=_AdGenESCUTIRKSID_Object((1,3,6,1,4,1,664,5,17,3,1,1,10),_AdGenESCUTIRKSID_Type())
adGenESCUTIRKSID.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenESCUTIRKSID.setStatus(_A)
_AdGenESCUTest_ObjectIdentity=ObjectIdentity
adGenESCUTest=_AdGenESCUTest_ObjectIdentity((1,3,6,1,4,1,664,5,17,4))
_AdGenESCUTestTable_Object=MibTable
adGenESCUTestTable=_AdGenESCUTestTable_Object((1,3,6,1,4,1,664,5,17,4,1))
if mibBuilder.loadTexts:adGenESCUTestTable.setStatus(_A)
_AdGenESCUTestEntry_Object=MibTableRow
adGenESCUTestEntry=_AdGenESCUTestEntry_Object((1,3,6,1,4,1,664,5,17,4,1,1))
adGenESCUTestEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:adGenESCUTestEntry.setStatus(_A)
class _AdGenESCUReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_AdGenESCUReset_Type.__name__=_B
_AdGenESCUReset_Object=MibTableColumn
adGenESCUReset=_AdGenESCUReset_Object((1,3,6,1,4,1,664,5,17,4,1,1,1),_AdGenESCUReset_Type())
adGenESCUReset.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenESCUReset.setStatus(_A)
_AdGenESCUselfTestResults_Type=DisplayString
_AdGenESCUselfTestResults_Object=MibTableColumn
adGenESCUselfTestResults=_AdGenESCUselfTestResults_Object((1,3,6,1,4,1,664,5,17,4,1,1,2),_AdGenESCUselfTestResults_Type())
adGenESCUselfTestResults.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenESCUselfTestResults.setStatus(_A)
class _AdGenESCUChassisLampTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('initiate',1))
_AdGenESCUChassisLampTest_Type.__name__=_B
_AdGenESCUChassisLampTest_Object=MibTableColumn
adGenESCUChassisLampTest=_AdGenESCUChassisLampTest_Object((1,3,6,1,4,1,664,5,17,4,1,1,3),_AdGenESCUChassisLampTest_Type())
adGenESCUChassisLampTest.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenESCUChassisLampTest.setStatus(_A)
mibBuilder.exportSymbols('ADTRAN-GENESCU-MIB',**{'adGenESCUmg':adGenESCUmg,'adGenESCUConfig':adGenESCUConfig,'adGenESCUProv':adGenESCUProv,'adGenESCUProvTable':adGenESCUProvTable,'adGenESCUProvEntry':adGenESCUProvEntry,'adGenESCUadminPortRate':adGenESCUadminPortRate,'adGenESCUautoLogoff':adGenESCUautoLogoff,'adGenESCUautoLogoffTimer':adGenESCUautoLogoffTimer,'adGenESCUmoduleAutoProv':adGenESCUmoduleAutoProv,'adGenESCUmuxAutoProv':adGenESCUmuxAutoProv,'adGenESCUrestoreFactoryDefaults':adGenESCUrestoreFactoryDefaults,'adGenESCUadminPortMode':adGenESCUadminPortMode,'adGenESCUcraftPortRate':adGenESCUcraftPortRate,'adGenESCUadminSecurityEnable':adGenESCUadminSecurityEnable,'adGenESCUStatus':adGenESCUStatus,'adGenESCUStatusTable':adGenESCUStatusTable,'adGenESCUStatusEntry':adGenESCUStatusEntry,'adGenESCUacoStatus':adGenESCUacoStatus,'adGenESCUacoinStatus':adGenESCUacoinStatus,'adGenESCUrmtinStatus':adGenESCUrmtinStatus,'adGenESCUextin1Status':adGenESCUextin1Status,'adGenESCUextin2Status':adGenESCUextin2Status,'adGenESCUminus48PowerAStatus':adGenESCUminus48PowerAStatus,'adGenESCUminus48PowerBStatus':adGenESCUminus48PowerBStatus,'adGenESCUopenFuseStatus':adGenESCUopenFuseStatus,'adGenESCUCLLI':adGenESCUCLLI,'adGenESCUTIRKSID':adGenESCUTIRKSID,'adGenESCUTest':adGenESCUTest,'adGenESCUTestTable':adGenESCUTestTable,'adGenESCUTestEntry':adGenESCUTestEntry,'adGenESCUReset':adGenESCUReset,'adGenESCUselfTestResults':adGenESCUselfTestResults,'adGenESCUChassisLampTest':adGenESCUChassisLampTest})