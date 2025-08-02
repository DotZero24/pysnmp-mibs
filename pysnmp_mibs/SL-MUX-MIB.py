_E='muxIfIndex'
_D='SL-MUX-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
CleiCode,=mibBuilder.importSymbols('SL-ENTITY-MIB','CleiCode')
sitelight,=mibBuilder.importSymbols('SL-NE-MIB','sitelight')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
slMux=ModuleIdentity((1,3,6,1,4,1,4515,1,5))
_MuxIfTable_Object=MibTable
muxIfTable=_MuxIfTable_Object((1,3,6,1,4,1,4515,1,5,1))
if mibBuilder.loadTexts:muxIfTable.setStatus(_A)
_MuxIfEntry_Object=MibTableRow
muxIfEntry=_MuxIfEntry_Object((1,3,6,1,4,1,4515,1,5,1,1))
muxIfEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:muxIfEntry.setStatus(_A)
_MuxIfIndex_Type=InterfaceIndex
_MuxIfIndex_Object=MibTableColumn
muxIfIndex=_MuxIfIndex_Object((1,3,6,1,4,1,4515,1,5,1,1,1),_MuxIfIndex_Type())
muxIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:muxIfIndex.setStatus(_A)
_MuxIfType_Type=Integer32
_MuxIfType_Object=MibTableColumn
muxIfType=_MuxIfType_Object((1,3,6,1,4,1,4515,1,5,1,1,2),_MuxIfType_Type())
muxIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:muxIfType.setStatus(_A)
class _MuxIfWaveSpacing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('ghzNone',0),('ghz400',1),('ghz200',2),('ghz100',3),('ghz50',4),('ghz2500',5)))
_MuxIfWaveSpacing_Type.__name__=_C
_MuxIfWaveSpacing_Object=MibTableColumn
muxIfWaveSpacing=_MuxIfWaveSpacing_Object((1,3,6,1,4,1,4515,1,5,1,1,3),_MuxIfWaveSpacing_Type())
muxIfWaveSpacing.setMaxAccess(_B)
if mibBuilder.loadTexts:muxIfWaveSpacing.setStatus(_A)
_MuxIfWaveLengthNm_Type=Integer32
_MuxIfWaveLengthNm_Object=MibTableColumn
muxIfWaveLengthNm=_MuxIfWaveLengthNm_Object((1,3,6,1,4,1,4515,1,5,1,1,4),_MuxIfWaveLengthNm_Type())
muxIfWaveLengthNm.setMaxAccess(_B)
if mibBuilder.loadTexts:muxIfWaveLengthNm.setStatus(_A)
_MuxIfOscWaveLengthNm_Type=Integer32
_MuxIfOscWaveLengthNm_Object=MibTableColumn
muxIfOscWaveLengthNm=_MuxIfOscWaveLengthNm_Object((1,3,6,1,4,1,4515,1,5,1,1,5),_MuxIfOscWaveLengthNm_Type())
muxIfOscWaveLengthNm.setMaxAccess(_B)
if mibBuilder.loadTexts:muxIfOscWaveLengthNm.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'slMux':slMux,'muxIfTable':muxIfTable,'muxIfEntry':muxIfEntry,_E:muxIfIndex,'muxIfType':muxIfType,'muxIfWaveSpacing':muxIfWaveSpacing,'muxIfWaveLengthNm':muxIfWaveLengthNm,'muxIfOscWaveLengthNm':muxIfOscWaveLengthNm})