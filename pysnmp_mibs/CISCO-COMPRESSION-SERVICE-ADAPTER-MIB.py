_Q='csaMIBGroup'
_P='csaEnable'
_O='csaDecompressionRatio'
_N='csaCompressionRatio'
_M='csaNumberOfRestarts'
_L='csaOutPacketsDrop'
_K='csaInPacketsDrop'
_J='csaOutPackets'
_I='csaInPackets'
_H='csaOutOctets'
_G='csaInOctets'
_F='cardIndex'
_E='OLD-CISCO-CHASSIS-MIB'
_D='Gauge32'
_C='read-only'
_B='CISCO-COMPRESSION-SERVICE-ADAPTER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
cardIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_D,'Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoCompressionServiceAdapterMIB=ModuleIdentity((1,3,6,1,4,1,9,9,57))
_CiscoCSAMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCSAMIBObjects=_CiscoCSAMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,57,1))
_CsaStats_ObjectIdentity=ObjectIdentity
csaStats=_CsaStats_ObjectIdentity((1,3,6,1,4,1,9,9,57,1,1))
_CsaStatsTable_Object=MibTable
csaStatsTable=_CsaStatsTable_Object((1,3,6,1,4,1,9,9,57,1,1,1))
if mibBuilder.loadTexts:csaStatsTable.setStatus(_A)
_CsaStatsEntry_Object=MibTableRow
csaStatsEntry=_CsaStatsEntry_Object((1,3,6,1,4,1,9,9,57,1,1,1,1))
csaStatsEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:csaStatsEntry.setStatus(_A)
_CsaInOctets_Type=Counter32
_CsaInOctets_Object=MibTableColumn
csaInOctets=_CsaInOctets_Object((1,3,6,1,4,1,9,9,57,1,1,1,1,1),_CsaInOctets_Type())
csaInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:csaInOctets.setStatus(_A)
_CsaOutOctets_Type=Counter32
_CsaOutOctets_Object=MibTableColumn
csaOutOctets=_CsaOutOctets_Object((1,3,6,1,4,1,9,9,57,1,1,1,1,2),_CsaOutOctets_Type())
csaOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:csaOutOctets.setStatus(_A)
_CsaInPackets_Type=Counter32
_CsaInPackets_Object=MibTableColumn
csaInPackets=_CsaInPackets_Object((1,3,6,1,4,1,9,9,57,1,1,1,1,3),_CsaInPackets_Type())
csaInPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:csaInPackets.setStatus(_A)
_CsaOutPackets_Type=Counter32
_CsaOutPackets_Object=MibTableColumn
csaOutPackets=_CsaOutPackets_Object((1,3,6,1,4,1,9,9,57,1,1,1,1,4),_CsaOutPackets_Type())
csaOutPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:csaOutPackets.setStatus(_A)
_CsaInPacketsDrop_Type=Counter32
_CsaInPacketsDrop_Object=MibTableColumn
csaInPacketsDrop=_CsaInPacketsDrop_Object((1,3,6,1,4,1,9,9,57,1,1,1,1,5),_CsaInPacketsDrop_Type())
csaInPacketsDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:csaInPacketsDrop.setStatus(_A)
_CsaOutPacketsDrop_Type=Counter32
_CsaOutPacketsDrop_Object=MibTableColumn
csaOutPacketsDrop=_CsaOutPacketsDrop_Object((1,3,6,1,4,1,9,9,57,1,1,1,1,6),_CsaOutPacketsDrop_Type())
csaOutPacketsDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:csaOutPacketsDrop.setStatus(_A)
_CsaNumberOfRestarts_Type=Counter32
_CsaNumberOfRestarts_Object=MibTableColumn
csaNumberOfRestarts=_CsaNumberOfRestarts_Object((1,3,6,1,4,1,9,9,57,1,1,1,1,7),_CsaNumberOfRestarts_Type())
csaNumberOfRestarts.setMaxAccess(_C)
if mibBuilder.loadTexts:csaNumberOfRestarts.setStatus(_A)
class _CsaCompressionRatio_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CsaCompressionRatio_Type.__name__=_D
_CsaCompressionRatio_Object=MibTableColumn
csaCompressionRatio=_CsaCompressionRatio_Object((1,3,6,1,4,1,9,9,57,1,1,1,1,8),_CsaCompressionRatio_Type())
csaCompressionRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:csaCompressionRatio.setStatus(_A)
class _CsaDecompressionRatio_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CsaDecompressionRatio_Type.__name__=_D
_CsaDecompressionRatio_Object=MibTableColumn
csaDecompressionRatio=_CsaDecompressionRatio_Object((1,3,6,1,4,1,9,9,57,1,1,1,1,9),_CsaDecompressionRatio_Type())
csaDecompressionRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:csaDecompressionRatio.setStatus(_A)
_CsaEnable_Type=TruthValue
_CsaEnable_Object=MibTableColumn
csaEnable=_CsaEnable_Object((1,3,6,1,4,1,9,9,57,1,1,1,1,10),_CsaEnable_Type())
csaEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:csaEnable.setStatus(_A)
_CiscoCSAMIBConformance_ObjectIdentity=ObjectIdentity
ciscoCSAMIBConformance=_CiscoCSAMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,57,3))
_CsaMIBCompliances_ObjectIdentity=ObjectIdentity
csaMIBCompliances=_CsaMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,57,3,1))
_CsaMIBGroups_ObjectIdentity=ObjectIdentity
csaMIBGroups=_CsaMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,57,3,2))
csaMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,57,3,2,1))
csaMIBGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:csaMIBGroup.setStatus(_A)
csaMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,57,3,1,1))
csaMIBCompliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:csaMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoCompressionServiceAdapterMIB':ciscoCompressionServiceAdapterMIB,'ciscoCSAMIBObjects':ciscoCSAMIBObjects,'csaStats':csaStats,'csaStatsTable':csaStatsTable,'csaStatsEntry':csaStatsEntry,_G:csaInOctets,_H:csaOutOctets,_I:csaInPackets,_J:csaOutPackets,_K:csaInPacketsDrop,_L:csaOutPacketsDrop,_M:csaNumberOfRestarts,_N:csaCompressionRatio,_O:csaDecompressionRatio,_P:csaEnable,'ciscoCSAMIBConformance':ciscoCSAMIBConformance,'csaMIBCompliances':csaMIBCompliances,'csaMIBCompliance':csaMIBCompliance,'csaMIBGroups':csaMIBGroups,_Q:csaMIBGroup})