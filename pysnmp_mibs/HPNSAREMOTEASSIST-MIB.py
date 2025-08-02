_M='hpnsaRALogIndex'
_L='hpnsaRAVoltTypeIndex'
_K='hpnsaRAAgentIndex'
_J='NotificationType'
_I='OctetString'
_H='HPNSAREMOTEASSIST-MIB'
_G='DisplayString'
_F='read-write'
_E='enabled'
_D='disabled'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_J,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_J,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_Hpnsa_ObjectIdentity=ObjectIdentity
hpnsa=_Hpnsa_ObjectIdentity((1,3,6,1,4,1,11,2,23))
_HpnsaRemoteAssist_ObjectIdentity=ObjectIdentity
hpnsaRemoteAssist=_HpnsaRemoteAssist_ObjectIdentity((1,3,6,1,4,1,11,2,23,8))
_HpnsaRAMibRev_ObjectIdentity=ObjectIdentity
hpnsaRAMibRev=_HpnsaRAMibRev_ObjectIdentity((1,3,6,1,4,1,11,2,23,8,1))
class _HpnsaRAMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnsaRAMibRevMajor_Type.__name__=_C
_HpnsaRAMibRevMajor_Object=MibScalar
hpnsaRAMibRevMajor=_HpnsaRAMibRevMajor_Object((1,3,6,1,4,1,11,2,23,8,1,1),_HpnsaRAMibRevMajor_Type())
hpnsaRAMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRAMibRevMajor.setStatus(_A)
class _HpnsaRAMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaRAMibRevMinor_Type.__name__=_C
_HpnsaRAMibRevMinor_Object=MibScalar
hpnsaRAMibRevMinor=_HpnsaRAMibRevMinor_Object((1,3,6,1,4,1,11,2,23,8,1,2),_HpnsaRAMibRevMinor_Type())
hpnsaRAMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRAMibRevMinor.setStatus(_A)
_HpnsaRAAgent_ObjectIdentity=ObjectIdentity
hpnsaRAAgent=_HpnsaRAAgent_ObjectIdentity((1,3,6,1,4,1,11,2,23,8,2))
_HpnsaRAAgentTable_Object=MibTable
hpnsaRAAgentTable=_HpnsaRAAgentTable_Object((1,3,6,1,4,1,11,2,23,8,2,1))
if mibBuilder.loadTexts:hpnsaRAAgentTable.setStatus(_A)
_HpnsaRAAgentEntry_Object=MibTableRow
hpnsaRAAgentEntry=_HpnsaRAAgentEntry_Object((1,3,6,1,4,1,11,2,23,8,2,1,1))
hpnsaRAAgentEntry.setIndexNames((0,_H,_K))
if mibBuilder.loadTexts:hpnsaRAAgentEntry.setStatus(_A)
class _HpnsaRAAgentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaRAAgentIndex_Type.__name__=_C
_HpnsaRAAgentIndex_Object=MibTableColumn
hpnsaRAAgentIndex=_HpnsaRAAgentIndex_Object((1,3,6,1,4,1,11,2,23,8,2,1,1,1),_HpnsaRAAgentIndex_Type())
hpnsaRAAgentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRAAgentIndex.setStatus(_A)
class _HpnsaRAAgentName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaRAAgentName_Type.__name__=_G
_HpnsaRAAgentName_Object=MibTableColumn
hpnsaRAAgentName=_HpnsaRAAgentName_Object((1,3,6,1,4,1,11,2,23,8,2,1,1,2),_HpnsaRAAgentName_Type())
hpnsaRAAgentName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRAAgentName.setStatus(_A)
class _HpnsaRAAgentVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_HpnsaRAAgentVersion_Type.__name__=_G
_HpnsaRAAgentVersion_Object=MibTableColumn
hpnsaRAAgentVersion=_HpnsaRAAgentVersion_Object((1,3,6,1,4,1,11,2,23,8,2,1,1,3),_HpnsaRAAgentVersion_Type())
hpnsaRAAgentVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRAAgentVersion.setStatus(_A)
class _HpnsaRAAgentDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_HpnsaRAAgentDate_Type.__name__=_I
_HpnsaRAAgentDate_Object=MibTableColumn
hpnsaRAAgentDate=_HpnsaRAAgentDate_Object((1,3,6,1,4,1,11,2,23,8,2,1,1,4),_HpnsaRAAgentDate_Type())
hpnsaRAAgentDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRAAgentDate.setStatus(_A)
_HpnsaRAInfo_ObjectIdentity=ObjectIdentity
hpnsaRAInfo=_HpnsaRAInfo_ObjectIdentity((1,3,6,1,4,1,11,2,23,8,3))
class _HpnsaRAInfoBoardType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_HpnsaRAInfoBoardType_Type.__name__=_G
_HpnsaRAInfoBoardType_Object=MibScalar
hpnsaRAInfoBoardType=_HpnsaRAInfoBoardType_Object((1,3,6,1,4,1,11,2,23,8,3,1),_HpnsaRAInfoBoardType_Type())
hpnsaRAInfoBoardType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRAInfoBoardType.setStatus(_A)
class _HpnsaRAInfoBoardName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_HpnsaRAInfoBoardName_Type.__name__=_G
_HpnsaRAInfoBoardName_Object=MibScalar
hpnsaRAInfoBoardName=_HpnsaRAInfoBoardName_Object((1,3,6,1,4,1,11,2,23,8,3,2),_HpnsaRAInfoBoardName_Type())
hpnsaRAInfoBoardName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRAInfoBoardName.setStatus(_A)
_HpnsaRAInfoBoardID_Type=Integer32
_HpnsaRAInfoBoardID_Object=MibScalar
hpnsaRAInfoBoardID=_HpnsaRAInfoBoardID_Object((1,3,6,1,4,1,11,2,23,8,3,3),_HpnsaRAInfoBoardID_Type())
hpnsaRAInfoBoardID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRAInfoBoardID.setStatus(_A)
class _HpnsaRAInfoBoardVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_HpnsaRAInfoBoardVersion_Type.__name__=_G
_HpnsaRAInfoBoardVersion_Object=MibScalar
hpnsaRAInfoBoardVersion=_HpnsaRAInfoBoardVersion_Object((1,3,6,1,4,1,11,2,23,8,3,4),_HpnsaRAInfoBoardVersion_Type())
hpnsaRAInfoBoardVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRAInfoBoardVersion.setStatus(_A)
_HpnsaRATemp_ObjectIdentity=ObjectIdentity
hpnsaRATemp=_HpnsaRATemp_ObjectIdentity((1,3,6,1,4,1,11,2,23,8,4))
_HpnsaRATempMeasured_Type=Integer32
_HpnsaRATempMeasured_Object=MibScalar
hpnsaRATempMeasured=_HpnsaRATempMeasured_Object((1,3,6,1,4,1,11,2,23,8,4,1),_HpnsaRATempMeasured_Type())
hpnsaRATempMeasured.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRATempMeasured.setStatus(_A)
_HpnsaRATempWarnLimit_Type=Integer32
_HpnsaRATempWarnLimit_Object=MibScalar
hpnsaRATempWarnLimit=_HpnsaRATempWarnLimit_Object((1,3,6,1,4,1,11,2,23,8,4,2),_HpnsaRATempWarnLimit_Type())
hpnsaRATempWarnLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRATempWarnLimit.setStatus(_A)
_HpnsaRATempGracefulSDLimit_Type=Integer32
_HpnsaRATempGracefulSDLimit_Object=MibScalar
hpnsaRATempGracefulSDLimit=_HpnsaRATempGracefulSDLimit_Object((1,3,6,1,4,1,11,2,23,8,4,3),_HpnsaRATempGracefulSDLimit_Type())
hpnsaRATempGracefulSDLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRATempGracefulSDLimit.setStatus(_A)
_HpnsaRATempCriticalSDLimit_Type=Integer32
_HpnsaRATempCriticalSDLimit_Object=MibScalar
hpnsaRATempCriticalSDLimit=_HpnsaRATempCriticalSDLimit_Object((1,3,6,1,4,1,11,2,23,8,4,4),_HpnsaRATempCriticalSDLimit_Type())
hpnsaRATempCriticalSDLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRATempCriticalSDLimit.setStatus(_A)
_HpnsaRAVolt_ObjectIdentity=ObjectIdentity
hpnsaRAVolt=_HpnsaRAVolt_ObjectIdentity((1,3,6,1,4,1,11,2,23,8,5))
_HpnsaRAVoltTable_Object=MibTable
hpnsaRAVoltTable=_HpnsaRAVoltTable_Object((1,3,6,1,4,1,11,2,23,8,5,1))
if mibBuilder.loadTexts:hpnsaRAVoltTable.setStatus(_A)
_HpnsaRAVoltEntry_Object=MibTableRow
hpnsaRAVoltEntry=_HpnsaRAVoltEntry_Object((1,3,6,1,4,1,11,2,23,8,5,1,1))
hpnsaRAVoltEntry.setIndexNames((0,_H,_L))
if mibBuilder.loadTexts:hpnsaRAVoltEntry.setStatus(_A)
class _HpnsaRAVoltTypeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('negative12v',1),('positive12v',2),('positive5v',3),('positive3v',4)))
_HpnsaRAVoltTypeIndex_Type.__name__=_C
_HpnsaRAVoltTypeIndex_Object=MibTableColumn
hpnsaRAVoltTypeIndex=_HpnsaRAVoltTypeIndex_Object((1,3,6,1,4,1,11,2,23,8,5,1,1,1),_HpnsaRAVoltTypeIndex_Type())
hpnsaRAVoltTypeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRAVoltTypeIndex.setStatus(_A)
_HpnsaRAVoltMeasured_Type=DisplayString
_HpnsaRAVoltMeasured_Object=MibTableColumn
hpnsaRAVoltMeasured=_HpnsaRAVoltMeasured_Object((1,3,6,1,4,1,11,2,23,8,5,1,1,2),_HpnsaRAVoltMeasured_Type())
hpnsaRAVoltMeasured.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRAVoltMeasured.setStatus(_A)
_HpnsaRAVoltLoLimit_Type=DisplayString
_HpnsaRAVoltLoLimit_Object=MibTableColumn
hpnsaRAVoltLoLimit=_HpnsaRAVoltLoLimit_Object((1,3,6,1,4,1,11,2,23,8,5,1,1,3),_HpnsaRAVoltLoLimit_Type())
hpnsaRAVoltLoLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRAVoltLoLimit.setStatus(_A)
_HpnsaRAVoltHiLimit_Type=DisplayString
_HpnsaRAVoltHiLimit_Object=MibTableColumn
hpnsaRAVoltHiLimit=_HpnsaRAVoltHiLimit_Object((1,3,6,1,4,1,11,2,23,8,5,1,1,4),_HpnsaRAVoltHiLimit_Type())
hpnsaRAVoltHiLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRAVoltHiLimit.setStatus(_A)
_HpnsaRABusUsage_ObjectIdentity=ObjectIdentity
hpnsaRABusUsage=_HpnsaRABusUsage_ObjectIdentity((1,3,6,1,4,1,11,2,23,8,6))
_HpnsaRABusUsage5SecAve_Type=Integer32
_HpnsaRABusUsage5SecAve_Object=MibScalar
hpnsaRABusUsage5SecAve=_HpnsaRABusUsage5SecAve_Object((1,3,6,1,4,1,11,2,23,8,6,1),_HpnsaRABusUsage5SecAve_Type())
hpnsaRABusUsage5SecAve.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRABusUsage5SecAve.setStatus(_A)
_HpnsaRABusUsage15SecAve_Type=Integer32
_HpnsaRABusUsage15SecAve_Object=MibScalar
hpnsaRABusUsage15SecAve=_HpnsaRABusUsage15SecAve_Object((1,3,6,1,4,1,11,2,23,8,6,2),_HpnsaRABusUsage15SecAve_Type())
hpnsaRABusUsage15SecAve.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRABusUsage15SecAve.setStatus(_A)
_HpnsaRABusUsage1MinAve_Type=Integer32
_HpnsaRABusUsage1MinAve_Object=MibScalar
hpnsaRABusUsage1MinAve=_HpnsaRABusUsage1MinAve_Object((1,3,6,1,4,1,11,2,23,8,6,3),_HpnsaRABusUsage1MinAve_Type())
hpnsaRABusUsage1MinAve.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRABusUsage1MinAve.setStatus(_A)
_HpnsaRABusUsage5MinAve_Type=Integer32
_HpnsaRABusUsage5MinAve_Object=MibScalar
hpnsaRABusUsage5MinAve=_HpnsaRABusUsage5MinAve_Object((1,3,6,1,4,1,11,2,23,8,6,4),_HpnsaRABusUsage5MinAve_Type())
hpnsaRABusUsage5MinAve.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRABusUsage5MinAve.setStatus(_A)
_HpnsaRABusUsageLimit_Type=Integer32
_HpnsaRABusUsageLimit_Object=MibScalar
hpnsaRABusUsageLimit=_HpnsaRABusUsageLimit_Object((1,3,6,1,4,1,11,2,23,8,6,5),_HpnsaRABusUsageLimit_Type())
hpnsaRABusUsageLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRABusUsageLimit.setStatus(_A)
_HpnsaRALog_ObjectIdentity=ObjectIdentity
hpnsaRALog=_HpnsaRALog_ObjectIdentity((1,3,6,1,4,1,11,2,23,8,7))
_HpnsaRALogTable_Object=MibTable
hpnsaRALogTable=_HpnsaRALogTable_Object((1,3,6,1,4,1,11,2,23,8,7,1))
if mibBuilder.loadTexts:hpnsaRALogTable.setStatus(_A)
_HpnsaRALogEntry_Object=MibTableRow
hpnsaRALogEntry=_HpnsaRALogEntry_Object((1,3,6,1,4,1,11,2,23,8,7,1,1))
hpnsaRALogEntry.setIndexNames((0,_H,_M))
if mibBuilder.loadTexts:hpnsaRALogEntry.setStatus(_A)
_HpnsaRALogIndex_Type=Integer32
_HpnsaRALogIndex_Object=MibTableColumn
hpnsaRALogIndex=_HpnsaRALogIndex_Object((1,3,6,1,4,1,11,2,23,8,7,1,1,1),_HpnsaRALogIndex_Type())
hpnsaRALogIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRALogIndex.setStatus(_A)
_HpnsaRALogEventCode_Type=Integer32
_HpnsaRALogEventCode_Object=MibTableColumn
hpnsaRALogEventCode=_HpnsaRALogEventCode_Object((1,3,6,1,4,1,11,2,23,8,7,1,1,2),_HpnsaRALogEventCode_Type())
hpnsaRALogEventCode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRALogEventCode.setStatus(_A)
class _HpnsaRALogDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaRALogDescription_Type.__name__=_G
_HpnsaRALogDescription_Object=MibTableColumn
hpnsaRALogDescription=_HpnsaRALogDescription_Object((1,3,6,1,4,1,11,2,23,8,7,1,1,3),_HpnsaRALogDescription_Type())
hpnsaRALogDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRALogDescription.setStatus(_A)
class _HpnsaRALogViewed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('new',0),('viewed',1)))
_HpnsaRALogViewed_Type.__name__=_C
_HpnsaRALogViewed_Object=MibTableColumn
hpnsaRALogViewed=_HpnsaRALogViewed_Object((1,3,6,1,4,1,11,2,23,8,7,1,1,4),_HpnsaRALogViewed_Type())
hpnsaRALogViewed.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRALogViewed.setStatus(_A)
class _HpnsaRALogDateTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_HpnsaRALogDateTime_Type.__name__=_I
_HpnsaRALogDateTime_Object=MibTableColumn
hpnsaRALogDateTime=_HpnsaRALogDateTime_Object((1,3,6,1,4,1,11,2,23,8,7,1,1,5),_HpnsaRALogDateTime_Type())
hpnsaRALogDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRALogDateTime.setStatus(_A)
_HpnsaRALogData_Type=Integer32
_HpnsaRALogData_Object=MibTableColumn
hpnsaRALogData=_HpnsaRALogData_Object((1,3,6,1,4,1,11,2,23,8,7,1,1,6),_HpnsaRALogData_Type())
hpnsaRALogData.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaRALogData.setStatus(_A)
_HpnsaRAEventConfig_ObjectIdentity=ObjectIdentity
hpnsaRAEventConfig=_HpnsaRAEventConfig_ObjectIdentity((1,3,6,1,4,1,11,2,23,8,8))
class _HpnsaRAEventConfigGlobal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_HpnsaRAEventConfigGlobal_Type.__name__=_C
_HpnsaRAEventConfigGlobal_Object=MibScalar
hpnsaRAEventConfigGlobal=_HpnsaRAEventConfigGlobal_Object((1,3,6,1,4,1,11,2,23,8,8,1),_HpnsaRAEventConfigGlobal_Type())
hpnsaRAEventConfigGlobal.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnsaRAEventConfigGlobal.setStatus(_A)
class _HpnsaRAEventConfigVolt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_HpnsaRAEventConfigVolt_Type.__name__=_C
_HpnsaRAEventConfigVolt_Object=MibScalar
hpnsaRAEventConfigVolt=_HpnsaRAEventConfigVolt_Object((1,3,6,1,4,1,11,2,23,8,8,2),_HpnsaRAEventConfigVolt_Type())
hpnsaRAEventConfigVolt.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnsaRAEventConfigVolt.setStatus(_A)
class _HpnsaRAEventConfigTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_HpnsaRAEventConfigTemp_Type.__name__=_C
_HpnsaRAEventConfigTemp_Object=MibScalar
hpnsaRAEventConfigTemp=_HpnsaRAEventConfigTemp_Object((1,3,6,1,4,1,11,2,23,8,8,3),_HpnsaRAEventConfigTemp_Type())
hpnsaRAEventConfigTemp.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnsaRAEventConfigTemp.setStatus(_A)
class _HpnsaRAEventConfigAsr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_HpnsaRAEventConfigAsr_Type.__name__=_C
_HpnsaRAEventConfigAsr_Object=MibScalar
hpnsaRAEventConfigAsr=_HpnsaRAEventConfigAsr_Object((1,3,6,1,4,1,11,2,23,8,8,4),_HpnsaRAEventConfigAsr_Type())
hpnsaRAEventConfigAsr.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnsaRAEventConfigAsr.setStatus(_A)
class _HpnsaRAEventConfigRemBoot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_HpnsaRAEventConfigRemBoot_Type.__name__=_C
_HpnsaRAEventConfigRemBoot_Object=MibScalar
hpnsaRAEventConfigRemBoot=_HpnsaRAEventConfigRemBoot_Object((1,3,6,1,4,1,11,2,23,8,8,5),_HpnsaRAEventConfigRemBoot_Type())
hpnsaRAEventConfigRemBoot.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnsaRAEventConfigRemBoot.setStatus(_A)
class _HpnsaRAEventConfigBusUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_HpnsaRAEventConfigBusUsage_Type.__name__=_C
_HpnsaRAEventConfigBusUsage_Object=MibScalar
hpnsaRAEventConfigBusUsage=_HpnsaRAEventConfigBusUsage_Object((1,3,6,1,4,1,11,2,23,8,8,6),_HpnsaRAEventConfigBusUsage_Type())
hpnsaRAEventConfigBusUsage.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnsaRAEventConfigBusUsage.setStatus(_A)
class _HpnsaRAEventConfigRemAsst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_HpnsaRAEventConfigRemAsst_Type.__name__=_C
_HpnsaRAEventConfigRemAsst_Object=MibScalar
hpnsaRAEventConfigRemAsst=_HpnsaRAEventConfigRemAsst_Object((1,3,6,1,4,1,11,2,23,8,8,7),_HpnsaRAEventConfigRemAsst_Type())
hpnsaRAEventConfigRemAsst.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnsaRAEventConfigRemAsst.setStatus(_A)
class _HpnsaRAEventConfigTrapTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_HpnsaRAEventConfigTrapTest_Type.__name__=_C
_HpnsaRAEventConfigTrapTest_Object=MibScalar
hpnsaRAEventConfigTrapTest=_HpnsaRAEventConfigTrapTest_Object((1,3,6,1,4,1,11,2,23,8,8,8),_HpnsaRAEventConfigTrapTest_Type())
hpnsaRAEventConfigTrapTest.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnsaRAEventConfigTrapTest.setStatus(_A)
class _HpnsaRAEventConfigHostSys_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_HpnsaRAEventConfigHostSys_Type.__name__=_C
_HpnsaRAEventConfigHostSys_Object=MibScalar
hpnsaRAEventConfigHostSys=_HpnsaRAEventConfigHostSys_Object((1,3,6,1,4,1,11,2,23,8,8,9),_HpnsaRAEventConfigHostSys_Type())
hpnsaRAEventConfigHostSys.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnsaRAEventConfigHostSys.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'hp':hp,'nm':nm,'hpnsa':hpnsa,'hpnsaRemoteAssist':hpnsaRemoteAssist,'hpnsaRAMibRev':hpnsaRAMibRev,'hpnsaRAMibRevMajor':hpnsaRAMibRevMajor,'hpnsaRAMibRevMinor':hpnsaRAMibRevMinor,'hpnsaRAAgent':hpnsaRAAgent,'hpnsaRAAgentTable':hpnsaRAAgentTable,'hpnsaRAAgentEntry':hpnsaRAAgentEntry,_K:hpnsaRAAgentIndex,'hpnsaRAAgentName':hpnsaRAAgentName,'hpnsaRAAgentVersion':hpnsaRAAgentVersion,'hpnsaRAAgentDate':hpnsaRAAgentDate,'hpnsaRAInfo':hpnsaRAInfo,'hpnsaRAInfoBoardType':hpnsaRAInfoBoardType,'hpnsaRAInfoBoardName':hpnsaRAInfoBoardName,'hpnsaRAInfoBoardID':hpnsaRAInfoBoardID,'hpnsaRAInfoBoardVersion':hpnsaRAInfoBoardVersion,'hpnsaRATemp':hpnsaRATemp,'hpnsaRATempMeasured':hpnsaRATempMeasured,'hpnsaRATempWarnLimit':hpnsaRATempWarnLimit,'hpnsaRATempGracefulSDLimit':hpnsaRATempGracefulSDLimit,'hpnsaRATempCriticalSDLimit':hpnsaRATempCriticalSDLimit,'hpnsaRAVolt':hpnsaRAVolt,'hpnsaRAVoltTable':hpnsaRAVoltTable,'hpnsaRAVoltEntry':hpnsaRAVoltEntry,_L:hpnsaRAVoltTypeIndex,'hpnsaRAVoltMeasured':hpnsaRAVoltMeasured,'hpnsaRAVoltLoLimit':hpnsaRAVoltLoLimit,'hpnsaRAVoltHiLimit':hpnsaRAVoltHiLimit,'hpnsaRABusUsage':hpnsaRABusUsage,'hpnsaRABusUsage5SecAve':hpnsaRABusUsage5SecAve,'hpnsaRABusUsage15SecAve':hpnsaRABusUsage15SecAve,'hpnsaRABusUsage1MinAve':hpnsaRABusUsage1MinAve,'hpnsaRABusUsage5MinAve':hpnsaRABusUsage5MinAve,'hpnsaRABusUsageLimit':hpnsaRABusUsageLimit,'hpnsaRALog':hpnsaRALog,'hpnsaRALogTable':hpnsaRALogTable,'hpnsaRALogEntry':hpnsaRALogEntry,_M:hpnsaRALogIndex,'hpnsaRALogEventCode':hpnsaRALogEventCode,'hpnsaRALogDescription':hpnsaRALogDescription,'hpnsaRALogViewed':hpnsaRALogViewed,'hpnsaRALogDateTime':hpnsaRALogDateTime,'hpnsaRALogData':hpnsaRALogData,'hpnsaRAEventConfig':hpnsaRAEventConfig,'hpnsaRAEventConfigGlobal':hpnsaRAEventConfigGlobal,'hpnsaRAEventConfigVolt':hpnsaRAEventConfigVolt,'hpnsaRAEventConfigTemp':hpnsaRAEventConfigTemp,'hpnsaRAEventConfigAsr':hpnsaRAEventConfigAsr,'hpnsaRAEventConfigRemBoot':hpnsaRAEventConfigRemBoot,'hpnsaRAEventConfigBusUsage':hpnsaRAEventConfigBusUsage,'hpnsaRAEventConfigRemAsst':hpnsaRAEventConfigRemAsst,'hpnsaRAEventConfigTrapTest':hpnsaRAEventConfigTrapTest,'hpnsaRAEventConfigHostSys':hpnsaRAEventConfigHostSys})