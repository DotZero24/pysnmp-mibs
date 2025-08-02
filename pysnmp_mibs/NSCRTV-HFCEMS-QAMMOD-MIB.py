_H='qamModDCPowerIndex'
_G='qamPidFilterIndex'
_F='NSCRTV-HFCEMS-QAMMOD-MIB'
_E='optional'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qammodIdent,=mibBuilder.importSymbols('NSCRTV-ROOT','qammodIdent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_QamModVendorOID_Type=ObjectIdentifier
_QamModVendorOID_Object=MibScalar
qamModVendorOID=_QamModVendorOID_Object((1,3,6,1,4,1,17409,1,5,1),_QamModVendorOID_Type())
qamModVendorOID.setMaxAccess(_C)
if mibBuilder.loadTexts:qamModVendorOID.setStatus(_E)
class _QamModmode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_QamModmode_Type.__name__=_B
_QamModmode_Object=MibScalar
qamModmode=_QamModmode_Object((1,3,6,1,4,1,17409,1,5,2),_QamModmode_Type())
qamModmode.setMaxAccess(_D)
if mibBuilder.loadTexts:qamModmode.setStatus(_A)
class _QamModsymbolrate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QamModsymbolrate_Type.__name__=_B
_QamModsymbolrate_Object=MibScalar
qamModsymbolrate=_QamModsymbolrate_Object((1,3,6,1,4,1,17409,1,5,3),_QamModsymbolrate_Type())
qamModsymbolrate.setMaxAccess(_D)
if mibBuilder.loadTexts:qamModsymbolrate.setStatus(_A)
_QamModRFfreq_Type=Integer32
_QamModRFfreq_Object=MibScalar
qamModRFfreq=_QamModRFfreq_Object((1,3,6,1,4,1,17409,1,5,4),_QamModRFfreq_Type())
qamModRFfreq.setMaxAccess(_D)
if mibBuilder.loadTexts:qamModRFfreq.setStatus(_A)
_QamModRFLevel_Type=Integer32
_QamModRFLevel_Object=MibScalar
qamModRFLevel=_QamModRFLevel_Object((1,3,6,1,4,1,17409,1,5,5),_QamModRFLevel_Type())
qamModRFLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:qamModRFLevel.setStatus(_E)
_QamModRFLevelatt_Type=Integer32
_QamModRFLevelatt_Object=MibScalar
qamModRFLevelatt=_QamModRFLevelatt_Object((1,3,6,1,4,1,17409,1,5,6),_QamModRFLevelatt_Type())
qamModRFLevelatt.setMaxAccess(_D)
if mibBuilder.loadTexts:qamModRFLevelatt.setStatus(_E)
class _QamModInputInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('asi',1),('spi',2),('ds3',3),('other',4)))
_QamModInputInterface_Type.__name__=_B
_QamModInputInterface_Object=MibScalar
qamModInputInterface=_QamModInputInterface_Object((1,3,6,1,4,1,17409,1,5,7),_QamModInputInterface_Type())
qamModInputInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:qamModInputInterface.setStatus(_A)
class _QamInputstatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sync',1),('noSync',2)))
_QamInputstatus_Type.__name__=_B
_QamInputstatus_Object=MibScalar
qamInputstatus=_QamInputstatus_Object((1,3,6,1,4,1,17409,1,5,8),_QamInputstatus_Type())
qamInputstatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qamInputstatus.setStatus(_A)
class _QamModTSpacketlen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bytes188',1),('bytes204',2)))
_QamModTSpacketlen_Type.__name__=_B
_QamModTSpacketlen_Object=MibScalar
qamModTSpacketlen=_QamModTSpacketlen_Object((1,3,6,1,4,1,17409,1,5,9),_QamModTSpacketlen_Type())
qamModTSpacketlen.setMaxAccess(_D)
if mibBuilder.loadTexts:qamModTSpacketlen.setStatus(_A)
_QamPidFilterTable_Object=MibTable
qamPidFilterTable=_QamPidFilterTable_Object((1,3,6,1,4,1,17409,1,5,10))
if mibBuilder.loadTexts:qamPidFilterTable.setStatus(_A)
_QamPidFilterEntry_Object=MibTableRow
qamPidFilterEntry=_QamPidFilterEntry_Object((1,3,6,1,4,1,17409,1,5,10,1))
qamPidFilterEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:qamPidFilterEntry.setStatus(_A)
_QamPidFilterIndex_Type=Integer32
_QamPidFilterIndex_Object=MibTableColumn
qamPidFilterIndex=_QamPidFilterIndex_Object((1,3,6,1,4,1,17409,1,5,10,1,1),_QamPidFilterIndex_Type())
qamPidFilterIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qamPidFilterIndex.setStatus(_A)
class _QamInPid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_QamInPid_Type.__name__=_B
_QamInPid_Object=MibTableColumn
qamInPid=_QamInPid_Object((1,3,6,1,4,1,17409,1,5,10,1,2),_QamInPid_Type())
qamInPid.setMaxAccess(_C)
if mibBuilder.loadTexts:qamInPid.setStatus(_A)
class _QamModNumberDCPowerSupply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QamModNumberDCPowerSupply_Type.__name__=_B
_QamModNumberDCPowerSupply_Object=MibScalar
qamModNumberDCPowerSupply=_QamModNumberDCPowerSupply_Object((1,3,6,1,4,1,17409,1,5,11),_QamModNumberDCPowerSupply_Type())
qamModNumberDCPowerSupply.setMaxAccess(_C)
if mibBuilder.loadTexts:qamModNumberDCPowerSupply.setStatus(_A)
class _QamModDCPowerSupplyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('loadsharing',1),('switchedRedundant',2),('aloneSupply',3)))
_QamModDCPowerSupplyMode_Type.__name__=_B
_QamModDCPowerSupplyMode_Object=MibScalar
qamModDCPowerSupplyMode=_QamModDCPowerSupplyMode_Object((1,3,6,1,4,1,17409,1,5,12),_QamModDCPowerSupplyMode_Type())
qamModDCPowerSupplyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:qamModDCPowerSupplyMode.setStatus(_E)
_QamModDCPowerTable_Object=MibTable
qamModDCPowerTable=_QamModDCPowerTable_Object((1,3,6,1,4,1,17409,1,5,13))
if mibBuilder.loadTexts:qamModDCPowerTable.setStatus(_A)
_QamModDCPowerEntry_Object=MibTableRow
qamModDCPowerEntry=_QamModDCPowerEntry_Object((1,3,6,1,4,1,17409,1,5,13,1))
qamModDCPowerEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:qamModDCPowerEntry.setStatus(_A)
_QamModDCPowerIndex_Type=Integer32
_QamModDCPowerIndex_Object=MibTableColumn
qamModDCPowerIndex=_QamModDCPowerIndex_Object((1,3,6,1,4,1,17409,1,5,13,1,1),_QamModDCPowerIndex_Type())
qamModDCPowerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qamModDCPowerIndex.setStatus(_A)
class _QamModDCPowerVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
_QamModDCPowerVoltage_Type.__name__=_B
_QamModDCPowerVoltage_Object=MibTableColumn
qamModDCPowerVoltage=_QamModDCPowerVoltage_Object((1,3,6,1,4,1,17409,1,5,13,1,2),_QamModDCPowerVoltage_Type())
qamModDCPowerVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:qamModDCPowerVoltage.setStatus(_A)
class _QamModDCPowerCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QamModDCPowerCurrent_Type.__name__=_B
_QamModDCPowerCurrent_Object=MibTableColumn
qamModDCPowerCurrent=_QamModDCPowerCurrent_Object((1,3,6,1,4,1,17409,1,5,13,1,3),_QamModDCPowerCurrent_Type())
qamModDCPowerCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:qamModDCPowerCurrent.setStatus(_E)
_QamModDCPowerName_Type=DisplayString
_QamModDCPowerName_Object=MibTableColumn
qamModDCPowerName=_QamModDCPowerName_Object((1,3,6,1,4,1,17409,1,5,13,1,4),_QamModDCPowerName_Type())
qamModDCPowerName.setMaxAccess(_C)
if mibBuilder.loadTexts:qamModDCPowerName.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'qamModVendorOID':qamModVendorOID,'qamModmode':qamModmode,'qamModsymbolrate':qamModsymbolrate,'qamModRFfreq':qamModRFfreq,'qamModRFLevel':qamModRFLevel,'qamModRFLevelatt':qamModRFLevelatt,'qamModInputInterface':qamModInputInterface,'qamInputstatus':qamInputstatus,'qamModTSpacketlen':qamModTSpacketlen,'qamPidFilterTable':qamPidFilterTable,'qamPidFilterEntry':qamPidFilterEntry,_G:qamPidFilterIndex,'qamInPid':qamInPid,'qamModNumberDCPowerSupply':qamModNumberDCPowerSupply,'qamModDCPowerSupplyMode':qamModDCPowerSupplyMode,'qamModDCPowerTable':qamModDCPowerTable,'qamModDCPowerEntry':qamModDCPowerEntry,_H:qamModDCPowerIndex,'qamModDCPowerVoltage':qamModDCPowerVoltage,'qamModDCPowerCurrent':qamModDCPowerCurrent,'qamModDCPowerName':qamModDCPowerName})