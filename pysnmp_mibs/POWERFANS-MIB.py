_F='powerNo'
_E='DisplayString'
_D='NotificationType'
_C='POWERFANS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso,mgmt=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_D,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_D,'TimeTicks','Unsigned32','enterprises','iso','mgmt')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
class FanStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('fan-online',0),('fan-offline',1)))
class PowerStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('power-work',0),('power-online',1),('power-offline',2)))
class DisplayString(OctetString):0
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_Zxr10_ObjectIdentity=ObjectIdentity
zxr10=_Zxr10_ObjectIdentity((1,3,6,1,4,1,3902,3))
_Zxr10systemconfig_ObjectIdentity=ObjectIdentity
zxr10systemconfig=_Zxr10systemconfig_ObjectIdentity((1,3,6,1,4,1,3902,3,1))
_Enviorment_ObjectIdentity=ObjectIdentity
enviorment=_Enviorment_ObjectIdentity((1,3,6,1,4,1,3902,3,200))
_FanTable_Object=MibTable
fanTable=_FanTable_Object((1,3,6,1,4,1,3902,3,200,1))
if mibBuilder.loadTexts:fanTable.setStatus(_A)
_FanEntry_Object=MibTableRow
fanEntry=_FanEntry_Object((1,3,6,1,4,1,3902,3,200,1,1))
fanEntry.setIndexNames((0,_C,'fanNo'))
if mibBuilder.loadTexts:fanEntry.setStatus(_A)
_FanNo_Type=Integer32
_FanNo_Object=MibTableColumn
fanNo=_FanNo_Object((1,3,6,1,4,1,3902,3,200,1,1,1),_FanNo_Type())
fanNo.setMaxAccess(_B)
if mibBuilder.loadTexts:fanNo.setStatus(_A)
_FanStat_Type=FanStatus
_FanStat_Object=MibTableColumn
fanStat=_FanStat_Object((1,3,6,1,4,1,3902,3,200,1,1,2),_FanStat_Type())
fanStat.setMaxAccess(_B)
if mibBuilder.loadTexts:fanStat.setStatus(_A)
_FanRotateSpeed_Type=Integer32
_FanRotateSpeed_Object=MibTableColumn
fanRotateSpeed=_FanRotateSpeed_Object((1,3,6,1,4,1,3902,3,200,1,1,3),_FanRotateSpeed_Type())
fanRotateSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:fanRotateSpeed.setStatus(_A)
_PowerTable_Object=MibTable
powerTable=_PowerTable_Object((1,3,6,1,4,1,3902,3,200,2))
if mibBuilder.loadTexts:powerTable.setStatus(_A)
_PowerEntry_Object=MibTableRow
powerEntry=_PowerEntry_Object((1,3,6,1,4,1,3902,3,200,2,1))
powerEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:powerEntry.setStatus(_A)
_PowerNo_Type=Integer32
_PowerNo_Object=MibTableColumn
powerNo=_PowerNo_Object((1,3,6,1,4,1,3902,3,200,2,1,1),_PowerNo_Type())
powerNo.setMaxAccess(_B)
if mibBuilder.loadTexts:powerNo.setStatus(_A)
_PowerStat_Type=PowerStatus
_PowerStat_Object=MibTableColumn
powerStat=_PowerStat_Object((1,3,6,1,4,1,3902,3,200,2,1,2),_PowerStat_Type())
powerStat.setMaxAccess(_B)
if mibBuilder.loadTexts:powerStat.setStatus(_A)
_PowerTemperature_Type=Integer32
_PowerTemperature_Object=MibTableColumn
powerTemperature=_PowerTemperature_Object((1,3,6,1,4,1,3902,3,200,2,1,3),_PowerTemperature_Type())
powerTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:powerTemperature.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'FanStatus':FanStatus,'PowerStatus':PowerStatus,_E:DisplayString,'zte':zte,'zxr10':zxr10,'zxr10systemconfig':zxr10systemconfig,'enviorment':enviorment,'fanTable':fanTable,'fanEntry':fanEntry,'fanNo':fanNo,'fanStat':fanStat,'fanRotateSpeed':fanRotateSpeed,'powerTable':powerTable,'powerEntry':powerEntry,_F:powerNo,'powerStat':powerStat,'powerTemperature':powerTemperature})