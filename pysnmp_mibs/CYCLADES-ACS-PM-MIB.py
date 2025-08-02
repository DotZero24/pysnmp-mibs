_K='unknow'
_J='cyOutletNumber'
_I='not-accessible'
_H='cyPMUnitNumber'
_G='DisplayString'
_F='Integer32'
_E='cyPMSerialPortNumber'
_D='read-write'
_C='CYCLADES-ACS-PM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cyACSMgmt,=mibBuilder.importSymbols('CYCLADES-ACS-MIB','cyACSMgmt')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
cyPM=ModuleIdentity((1,3,6,1,4,1,2925,4,5))
if mibBuilder.loadTexts:cyPM.setRevisions(('2005-08-29 00:00','2003-10-17 00:00'))
_CyNumberOfPM_Type=Integer32
_CyNumberOfPM_Object=MibScalar
cyNumberOfPM=_CyNumberOfPM_Object((1,3,6,1,4,1,2925,4,5,1),_CyNumberOfPM_Type())
cyNumberOfPM.setMaxAccess(_B)
if mibBuilder.loadTexts:cyNumberOfPM.setStatus(_A)
_CyPMTable_Object=MibTable
cyPMTable=_CyPMTable_Object((1,3,6,1,4,1,2925,4,5,2))
if mibBuilder.loadTexts:cyPMTable.setStatus(_A)
_CyPMEntry_Object=MibTableRow
cyPMEntry=_CyPMEntry_Object((1,3,6,1,4,1,2925,4,5,2,1))
cyPMEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cyPMEntry.setStatus(_A)
_CyPMSerialPortNumber_Type=InterfaceIndex
_CyPMSerialPortNumber_Object=MibTableColumn
cyPMSerialPortNumber=_CyPMSerialPortNumber_Object((1,3,6,1,4,1,2925,4,5,2,1,1),_CyPMSerialPortNumber_Type())
cyPMSerialPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cyPMSerialPortNumber.setStatus(_A)
_CyPMNumberOutlets_Type=Integer32
_CyPMNumberOutlets_Object=MibTableColumn
cyPMNumberOutlets=_CyPMNumberOutlets_Object((1,3,6,1,4,1,2925,4,5,2,1,2),_CyPMNumberOutlets_Type())
cyPMNumberOutlets.setMaxAccess(_B)
if mibBuilder.loadTexts:cyPMNumberOutlets.setStatus(_A)
_CyPMNumberUnits_Type=Integer32
_CyPMNumberUnits_Object=MibTableColumn
cyPMNumberUnits=_CyPMNumberUnits_Object((1,3,6,1,4,1,2925,4,5,2,1,3),_CyPMNumberUnits_Type())
cyPMNumberUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:cyPMNumberUnits.setStatus(_A)
_CyPMCurrent_Type=DisplayString
_CyPMCurrent_Object=MibTableColumn
cyPMCurrent=_CyPMCurrent_Object((1,3,6,1,4,1,2925,4,5,2,1,4),_CyPMCurrent_Type())
cyPMCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:cyPMCurrent.setStatus(_A)
_CyPMVersion_Type=DisplayString
_CyPMVersion_Object=MibTableColumn
cyPMVersion=_CyPMVersion_Object((1,3,6,1,4,1,2925,4,5,2,1,5),_CyPMVersion_Type())
cyPMVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cyPMVersion.setStatus(_A)
_CyPMTemperature_Type=DisplayString
_CyPMTemperature_Object=MibTableColumn
cyPMTemperature=_CyPMTemperature_Object((1,3,6,1,4,1,2925,4,5,2,1,6),_CyPMTemperature_Type())
cyPMTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:cyPMTemperature.setStatus(_A)
class _CyPMCommand_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_CyPMCommand_Type.__name__=_G
_CyPMCommand_Object=MibTableColumn
cyPMCommand=_CyPMCommand_Object((1,3,6,1,4,1,2925,4,5,2,1,7),_CyPMCommand_Type())
cyPMCommand.setMaxAccess(_D)
if mibBuilder.loadTexts:cyPMCommand.setStatus(_A)
_CyPMUnitTable_Object=MibTable
cyPMUnitTable=_CyPMUnitTable_Object((1,3,6,1,4,1,2925,4,5,3))
if mibBuilder.loadTexts:cyPMUnitTable.setStatus(_A)
_CyPMUnitEntry_Object=MibTableRow
cyPMUnitEntry=_CyPMUnitEntry_Object((1,3,6,1,4,1,2925,4,5,3,1))
cyPMUnitEntry.setIndexNames((0,_C,_E),(0,_C,_H))
if mibBuilder.loadTexts:cyPMUnitEntry.setStatus(_A)
_CyPMUnitNumber_Type=InterfaceIndex
_CyPMUnitNumber_Object=MibTableColumn
cyPMUnitNumber=_CyPMUnitNumber_Object((1,3,6,1,4,1,2925,4,5,3,1,1),_CyPMUnitNumber_Type())
cyPMUnitNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:cyPMUnitNumber.setStatus(_A)
_CyPMUnitVersion_Type=DisplayString
_CyPMUnitVersion_Object=MibTableColumn
cyPMUnitVersion=_CyPMUnitVersion_Object((1,3,6,1,4,1,2925,4,5,3,1,2),_CyPMUnitVersion_Type())
cyPMUnitVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cyPMUnitVersion.setStatus(_A)
_CyPMUnitOutlets_Type=Integer32
_CyPMUnitOutlets_Object=MibTableColumn
cyPMUnitOutlets=_CyPMUnitOutlets_Object((1,3,6,1,4,1,2925,4,5,3,1,3),_CyPMUnitOutlets_Type())
cyPMUnitOutlets.setMaxAccess(_B)
if mibBuilder.loadTexts:cyPMUnitOutlets.setStatus(_A)
_CyPMUnitFirstOutlet_Type=Integer32
_CyPMUnitFirstOutlet_Object=MibTableColumn
cyPMUnitFirstOutlet=_CyPMUnitFirstOutlet_Object((1,3,6,1,4,1,2925,4,5,3,1,4),_CyPMUnitFirstOutlet_Type())
cyPMUnitFirstOutlet.setMaxAccess(_B)
if mibBuilder.loadTexts:cyPMUnitFirstOutlet.setStatus(_A)
_CyPMUnitCurrent_Type=Integer32
_CyPMUnitCurrent_Object=MibTableColumn
cyPMUnitCurrent=_CyPMUnitCurrent_Object((1,3,6,1,4,1,2925,4,5,3,1,5),_CyPMUnitCurrent_Type())
cyPMUnitCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:cyPMUnitCurrent.setStatus(_A)
_CyPMUnitMaxCurrent_Type=Integer32
_CyPMUnitMaxCurrent_Object=MibTableColumn
cyPMUnitMaxCurrent=_CyPMUnitMaxCurrent_Object((1,3,6,1,4,1,2925,4,5,3,1,6),_CyPMUnitMaxCurrent_Type())
cyPMUnitMaxCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:cyPMUnitMaxCurrent.setStatus(_A)
_CyPMUnitTemperature_Type=Integer32
_CyPMUnitTemperature_Object=MibTableColumn
cyPMUnitTemperature=_CyPMUnitTemperature_Object((1,3,6,1,4,1,2925,4,5,3,1,7),_CyPMUnitTemperature_Type())
cyPMUnitTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:cyPMUnitTemperature.setStatus(_A)
_CyPMUnitMaxTemperature_Type=Integer32
_CyPMUnitMaxTemperature_Object=MibTableColumn
cyPMUnitMaxTemperature=_CyPMUnitMaxTemperature_Object((1,3,6,1,4,1,2925,4,5,3,1,8),_CyPMUnitMaxTemperature_Type())
cyPMUnitMaxTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:cyPMUnitMaxTemperature.setStatus(_A)
_CyOutletTable_Object=MibTable
cyOutletTable=_CyOutletTable_Object((1,3,6,1,4,1,2925,4,5,4))
if mibBuilder.loadTexts:cyOutletTable.setStatus(_A)
_CyOutletEntry_Object=MibTableRow
cyOutletEntry=_CyOutletEntry_Object((1,3,6,1,4,1,2925,4,5,4,1))
cyOutletEntry.setIndexNames((0,_C,_E),(0,_C,_J))
if mibBuilder.loadTexts:cyOutletEntry.setStatus(_A)
_CyOutletNumber_Type=InterfaceIndexOrZero
_CyOutletNumber_Object=MibTableColumn
cyOutletNumber=_CyOutletNumber_Object((1,3,6,1,4,1,2925,4,5,4,1,1),_CyOutletNumber_Type())
cyOutletNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:cyOutletNumber.setStatus(_A)
class _CyOutletName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_CyOutletName_Type.__name__=_G
_CyOutletName_Object=MibTableColumn
cyOutletName=_CyOutletName_Object((1,3,6,1,4,1,2925,4,5,4,1,2),_CyOutletName_Type())
cyOutletName.setMaxAccess(_D)
if mibBuilder.loadTexts:cyOutletName.setStatus(_A)
_CyOutletServer_Type=DisplayString
_CyOutletServer_Object=MibTableColumn
cyOutletServer=_CyOutletServer_Object((1,3,6,1,4,1,2925,4,5,4,1,3),_CyOutletServer_Type())
cyOutletServer.setMaxAccess(_B)
if mibBuilder.loadTexts:cyOutletServer.setStatus(_A)
class _CyOutletPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('off',0),('on',1),('cycle',2),(_K,3)))
_CyOutletPower_Type.__name__=_F
_CyOutletPower_Object=MibTableColumn
cyOutletPower=_CyOutletPower_Object((1,3,6,1,4,1,2925,4,5,4,1,4),_CyOutletPower_Type())
cyOutletPower.setMaxAccess(_D)
if mibBuilder.loadTexts:cyOutletPower.setStatus(_A)
class _CyOutletLock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unlock',0),('lock',1),(_K,2)))
_CyOutletLock_Type.__name__=_F
_CyOutletLock_Object=MibTableColumn
cyOutletLock=_CyOutletLock_Object((1,3,6,1,4,1,2925,4,5,4,1,5),_CyOutletLock_Type())
cyOutletLock.setMaxAccess(_D)
if mibBuilder.loadTexts:cyOutletLock.setStatus(_A)
_CyOutletPUInterval_Type=Integer32
_CyOutletPUInterval_Object=MibTableColumn
cyOutletPUInterval=_CyOutletPUInterval_Object((1,3,6,1,4,1,2925,4,5,4,1,6),_CyOutletPUInterval_Type())
cyOutletPUInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:cyOutletPUInterval.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cyPM':cyPM,'cyNumberOfPM':cyNumberOfPM,'cyPMTable':cyPMTable,'cyPMEntry':cyPMEntry,_E:cyPMSerialPortNumber,'cyPMNumberOutlets':cyPMNumberOutlets,'cyPMNumberUnits':cyPMNumberUnits,'cyPMCurrent':cyPMCurrent,'cyPMVersion':cyPMVersion,'cyPMTemperature':cyPMTemperature,'cyPMCommand':cyPMCommand,'cyPMUnitTable':cyPMUnitTable,'cyPMUnitEntry':cyPMUnitEntry,_H:cyPMUnitNumber,'cyPMUnitVersion':cyPMUnitVersion,'cyPMUnitOutlets':cyPMUnitOutlets,'cyPMUnitFirstOutlet':cyPMUnitFirstOutlet,'cyPMUnitCurrent':cyPMUnitCurrent,'cyPMUnitMaxCurrent':cyPMUnitMaxCurrent,'cyPMUnitTemperature':cyPMUnitTemperature,'cyPMUnitMaxTemperature':cyPMUnitMaxTemperature,'cyOutletTable':cyOutletTable,'cyOutletEntry':cyOutletEntry,_J:cyOutletNumber,'cyOutletName':cyOutletName,'cyOutletServer':cyOutletServer,'cyOutletPower':cyOutletPower,'cyOutletLock':cyOutletLock,'cyOutletPUInterval':cyOutletPUInterval})