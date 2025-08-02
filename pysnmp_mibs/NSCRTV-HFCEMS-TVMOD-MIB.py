_G='tvmodDCPowerIndex'
_F='NSCRTV-HFCEMS-TVMOD-MIB'
_E='optional'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
tvmodIdent,=mibBuilder.importSymbols('NSCRTV-ROOT','tvmodIdent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_TvmodVendorOID_Type=ObjectIdentifier
_TvmodVendorOID_Object=MibScalar
tvmodVendorOID=_TvmodVendorOID_Object((1,3,6,1,4,1,17409,1,4,1),_TvmodVendorOID_Type())
tvmodVendorOID.setMaxAccess(_C)
if mibBuilder.loadTexts:tvmodVendorOID.setStatus(_E)
class _TvmodOutputlevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TvmodOutputlevel_Type.__name__=_B
_TvmodOutputlevel_Object=MibScalar
tvmodOutputlevel=_TvmodOutputlevel_Object((1,3,6,1,4,1,17409,1,4,2),_TvmodOutputlevel_Type())
tvmodOutputlevel.setMaxAccess(_C)
if mibBuilder.loadTexts:tvmodOutputlevel.setStatus(_A)
class _TvmodOutputlevelAtt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TvmodOutputlevelAtt_Type.__name__=_B
_TvmodOutputlevelAtt_Object=MibScalar
tvmodOutputlevelAtt=_TvmodOutputlevelAtt_Object((1,3,6,1,4,1,17409,1,4,3),_TvmodOutputlevelAtt_Type())
tvmodOutputlevelAtt.setMaxAccess(_D)
if mibBuilder.loadTexts:tvmodOutputlevelAtt.setStatus(_A)
class _TvmodAVPower_ratio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,127))
_TvmodAVPower_ratio_Type.__name__=_B
_TvmodAVPower_ratio_Object=MibScalar
tvmodAVPower_ratio=_TvmodAVPower_ratio_Object((1,3,6,1,4,1,17409,1,4,4),_TvmodAVPower_ratio_Type())
tvmodAVPower_ratio.setMaxAccess(_D)
if mibBuilder.loadTexts:tvmodAVPower_ratio.setStatus(_A)
class _Tvmodfreqdeviation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Tvmodfreqdeviation_Type.__name__=_B
_Tvmodfreqdeviation_Object=MibScalar
tvmodfreqdeviation=_Tvmodfreqdeviation_Object((1,3,6,1,4,1,17409,1,4,5),_Tvmodfreqdeviation_Type())
tvmodfreqdeviation.setMaxAccess(_D)
if mibBuilder.loadTexts:tvmodfreqdeviation.setStatus(_A)
_TvmodOperatingFreq_Type=Integer32
_TvmodOperatingFreq_Object=MibScalar
tvmodOperatingFreq=_TvmodOperatingFreq_Object((1,3,6,1,4,1,17409,1,4,6),_TvmodOperatingFreq_Type())
tvmodOperatingFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:tvmodOperatingFreq.setStatus(_A)
class _TvmodModulatingDepth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_TvmodModulatingDepth_Type.__name__=_B
_TvmodModulatingDepth_Object=MibScalar
tvmodModulatingDepth=_TvmodModulatingDepth_Object((1,3,6,1,4,1,17409,1,4,7),_TvmodModulatingDepth_Type())
tvmodModulatingDepth.setMaxAccess(_D)
if mibBuilder.loadTexts:tvmodModulatingDepth.setStatus(_A)
class _TvmodLockalarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('alarm',2)))
_TvmodLockalarm_Type.__name__=_B
_TvmodLockalarm_Object=MibScalar
tvmodLockalarm=_TvmodLockalarm_Object((1,3,6,1,4,1,17409,1,4,8),_TvmodLockalarm_Type())
tvmodLockalarm.setMaxAccess(_C)
if mibBuilder.loadTexts:tvmodLockalarm.setStatus(_A)
class _TvmodNumberDCPowerSupply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_TvmodNumberDCPowerSupply_Type.__name__=_B
_TvmodNumberDCPowerSupply_Object=MibScalar
tvmodNumberDCPowerSupply=_TvmodNumberDCPowerSupply_Object((1,3,6,1,4,1,17409,1,4,9),_TvmodNumberDCPowerSupply_Type())
tvmodNumberDCPowerSupply.setMaxAccess(_C)
if mibBuilder.loadTexts:tvmodNumberDCPowerSupply.setStatus(_A)
class _TvmodDCPowerSupplymode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('loadsharing',1),('switchedRedundant',2)))
_TvmodDCPowerSupplymode_Type.__name__=_B
_TvmodDCPowerSupplymode_Object=MibScalar
tvmodDCPowerSupplymode=_TvmodDCPowerSupplymode_Object((1,3,6,1,4,1,17409,1,4,10),_TvmodDCPowerSupplymode_Type())
tvmodDCPowerSupplymode.setMaxAccess(_C)
if mibBuilder.loadTexts:tvmodDCPowerSupplymode.setStatus(_E)
_TvmodDCPowerTable_Object=MibTable
tvmodDCPowerTable=_TvmodDCPowerTable_Object((1,3,6,1,4,1,17409,1,4,11))
if mibBuilder.loadTexts:tvmodDCPowerTable.setStatus(_A)
_TvmodDCPowerEntry_Object=MibTableRow
tvmodDCPowerEntry=_TvmodDCPowerEntry_Object((1,3,6,1,4,1,17409,1,4,11,1))
tvmodDCPowerEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:tvmodDCPowerEntry.setStatus(_A)
_TvmodDCPowerIndex_Type=Integer32
_TvmodDCPowerIndex_Object=MibTableColumn
tvmodDCPowerIndex=_TvmodDCPowerIndex_Object((1,3,6,1,4,1,17409,1,4,11,1,1),_TvmodDCPowerIndex_Type())
tvmodDCPowerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tvmodDCPowerIndex.setStatus(_A)
class _TvmodDCPowerVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
_TvmodDCPowerVoltage_Type.__name__=_B
_TvmodDCPowerVoltage_Object=MibTableColumn
tvmodDCPowerVoltage=_TvmodDCPowerVoltage_Object((1,3,6,1,4,1,17409,1,4,11,1,2),_TvmodDCPowerVoltage_Type())
tvmodDCPowerVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:tvmodDCPowerVoltage.setStatus(_A)
class _TvmodDCPowerCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TvmodDCPowerCurrent_Type.__name__=_B
_TvmodDCPowerCurrent_Object=MibTableColumn
tvmodDCPowerCurrent=_TvmodDCPowerCurrent_Object((1,3,6,1,4,1,17409,1,4,11,1,3),_TvmodDCPowerCurrent_Type())
tvmodDCPowerCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:tvmodDCPowerCurrent.setStatus(_E)
_TvmodDCPowerName_Type=DisplayString
_TvmodDCPowerName_Object=MibTableColumn
tvmodDCPowerName=_TvmodDCPowerName_Object((1,3,6,1,4,1,17409,1,4,11,1,4),_TvmodDCPowerName_Type())
tvmodDCPowerName.setMaxAccess(_C)
if mibBuilder.loadTexts:tvmodDCPowerName.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'tvmodVendorOID':tvmodVendorOID,'tvmodOutputlevel':tvmodOutputlevel,'tvmodOutputlevelAtt':tvmodOutputlevelAtt,'tvmodAVPower-ratio':tvmodAVPower_ratio,'tvmodfreqdeviation':tvmodfreqdeviation,'tvmodOperatingFreq':tvmodOperatingFreq,'tvmodModulatingDepth':tvmodModulatingDepth,'tvmodLockalarm':tvmodLockalarm,'tvmodNumberDCPowerSupply':tvmodNumberDCPowerSupply,'tvmodDCPowerSupplymode':tvmodDCPowerSupplymode,'tvmodDCPowerTable':tvmodDCPowerTable,'tvmodDCPowerEntry':tvmodDCPowerEntry,_G:tvmodDCPowerIndex,'tvmodDCPowerVoltage':tvmodDCPowerVoltage,'tvmodDCPowerCurrent':tvmodDCPowerCurrent,'tvmodDCPowerName':tvmodDCPowerName})