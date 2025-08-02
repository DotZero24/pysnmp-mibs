_J='vertical'
_I='horizontal'
_H='dBm'
_G='aniBsuSuStatusMacAddr'
_F='BSUSUSTATUS-MIB'
_E='aniBsuWirelessPort'
_D='BSUWIRELESSIF-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aniBsuSuGroup,=mibBuilder.importSymbols('ANIROOT-MIB','aniBsuSuGroup')
aniBsuWirelessPort,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
aniBsuSuStatus=ModuleIdentity((1,3,6,1,4,1,4325,3,7,3))
_AniBsuSuUSLinkStatusTable_Object=MibTable
aniBsuSuUSLinkStatusTable=_AniBsuSuUSLinkStatusTable_Object((1,3,6,1,4,1,4325,3,7,3,1))
if mibBuilder.loadTexts:aniBsuSuUSLinkStatusTable.setStatus(_A)
_AniBsuSuUSLinkStatusEntry_Object=MibTableRow
aniBsuSuUSLinkStatusEntry=_AniBsuSuUSLinkStatusEntry_Object((1,3,6,1,4,1,4325,3,7,3,1,1))
aniBsuSuUSLinkStatusEntry.setIndexNames((0,_D,_E),(0,_F,_G))
if mibBuilder.loadTexts:aniBsuSuUSLinkStatusEntry.setStatus(_A)
_AniBsuSuStatusMacAddr_Type=MacAddress
_AniBsuSuStatusMacAddr_Object=MibTableColumn
aniBsuSuStatusMacAddr=_AniBsuSuStatusMacAddr_Object((1,3,6,1,4,1,4325,3,7,3,1,1,1),_AniBsuSuStatusMacAddr_Type())
aniBsuSuStatusMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuStatusMacAddr.setStatus(_A)
_AniBsuSuStatusIpAddr_Type=IpAddress
_AniBsuSuStatusIpAddr_Object=MibTableColumn
aniBsuSuStatusIpAddr=_AniBsuSuStatusIpAddr_Object((1,3,6,1,4,1,4325,3,7,3,1,1,2),_AniBsuSuStatusIpAddr_Type())
aniBsuSuStatusIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuStatusIpAddr.setStatus(_A)
class _AniBsuSuStatusUSPolarization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_AniBsuSuStatusUSPolarization_Type.__name__=_C
_AniBsuSuStatusUSPolarization_Object=MibTableColumn
aniBsuSuStatusUSPolarization=_AniBsuSuStatusUSPolarization_Object((1,3,6,1,4,1,4325,3,7,3,1,1,3),_AniBsuSuStatusUSPolarization_Type())
aniBsuSuStatusUSPolarization.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuStatusUSPolarization.setStatus(_A)
class _AniBsuSuStatusUSModulation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('qpsk',1),('qam16',2)))
_AniBsuSuStatusUSModulation_Type.__name__=_C
_AniBsuSuStatusUSModulation_Object=MibTableColumn
aniBsuSuStatusUSModulation=_AniBsuSuStatusUSModulation_Object((1,3,6,1,4,1,4325,3,7,3,1,1,4),_AniBsuSuStatusUSModulation_Type())
aniBsuSuStatusUSModulation.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuStatusUSModulation.setStatus(_A)
class _AniBsuSuStatusUSFec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('low',1),('high',2)))
_AniBsuSuStatusUSFec_Type.__name__=_C
_AniBsuSuStatusUSFec_Object=MibTableColumn
aniBsuSuStatusUSFec=_AniBsuSuStatusUSFec_Object((1,3,6,1,4,1,4325,3,7,3,1,1,5),_AniBsuSuStatusUSFec_Type())
aniBsuSuStatusUSFec.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuStatusUSFec.setStatus(_A)
class _AniBsuSuStatusSuTxPowerAttn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,62))
_AniBsuSuStatusSuTxPowerAttn_Type.__name__=_C
_AniBsuSuStatusSuTxPowerAttn_Object=MibTableColumn
aniBsuSuStatusSuTxPowerAttn=_AniBsuSuStatusSuTxPowerAttn_Object((1,3,6,1,4,1,4325,3,7,3,1,1,6),_AniBsuSuStatusSuTxPowerAttn_Type())
aniBsuSuStatusSuTxPowerAttn.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuStatusSuTxPowerAttn.setStatus(_A)
if mibBuilder.loadTexts:aniBsuSuStatusSuTxPowerAttn.setUnits('dB')
_AniBsuSuStatusUSRxPower_Type=Integer32
_AniBsuSuStatusUSRxPower_Object=MibTableColumn
aniBsuSuStatusUSRxPower=_AniBsuSuStatusUSRxPower_Object((1,3,6,1,4,1,4325,3,7,3,1,1,7),_AniBsuSuStatusUSRxPower_Type())
aniBsuSuStatusUSRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuStatusUSRxPower.setStatus(_A)
if mibBuilder.loadTexts:aniBsuSuStatusUSRxPower.setUnits(_H)
_AniBsuSuStatusSuTxPower_Type=Integer32
_AniBsuSuStatusSuTxPower_Object=MibTableColumn
aniBsuSuStatusSuTxPower=_AniBsuSuStatusSuTxPower_Object((1,3,6,1,4,1,4325,3,7,3,1,1,8),_AniBsuSuStatusSuTxPower_Type())
aniBsuSuStatusSuTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuStatusSuTxPower.setStatus(_A)
if mibBuilder.loadTexts:aniBsuSuStatusSuTxPower.setUnits(_H)
_AniBsuSuDSLinkStatusTable_Object=MibTable
aniBsuSuDSLinkStatusTable=_AniBsuSuDSLinkStatusTable_Object((1,3,6,1,4,1,4325,3,7,3,2))
if mibBuilder.loadTexts:aniBsuSuDSLinkStatusTable.setStatus(_A)
_AniBsuSuDSLinkStatusEntry_Object=MibTableRow
aniBsuSuDSLinkStatusEntry=_AniBsuSuDSLinkStatusEntry_Object((1,3,6,1,4,1,4325,3,7,3,2,1))
aniBsuSuDSLinkStatusEntry.setIndexNames((0,_D,_E),(0,_F,_G))
if mibBuilder.loadTexts:aniBsuSuDSLinkStatusEntry.setStatus(_A)
class _AniBsuSuStatusDSPolarization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_AniBsuSuStatusDSPolarization_Type.__name__=_C
_AniBsuSuStatusDSPolarization_Object=MibTableColumn
aniBsuSuStatusDSPolarization=_AniBsuSuStatusDSPolarization_Object((1,3,6,1,4,1,4325,3,7,3,2,1,1),_AniBsuSuStatusDSPolarization_Type())
aniBsuSuStatusDSPolarization.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuStatusDSPolarization.setStatus(_A)
class _AniBsuSuStatusDSModulation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('qpsk',1),('qam16',2)))
_AniBsuSuStatusDSModulation_Type.__name__=_C
_AniBsuSuStatusDSModulation_Object=MibTableColumn
aniBsuSuStatusDSModulation=_AniBsuSuStatusDSModulation_Object((1,3,6,1,4,1,4325,3,7,3,2,1,2),_AniBsuSuStatusDSModulation_Type())
aniBsuSuStatusDSModulation.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuStatusDSModulation.setStatus(_A)
class _AniBsuSuStatusDSFec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('low',1),('high',2)))
_AniBsuSuStatusDSFec_Type.__name__=_C
_AniBsuSuStatusDSFec_Object=MibTableColumn
aniBsuSuStatusDSFec=_AniBsuSuStatusDSFec_Object((1,3,6,1,4,1,4325,3,7,3,2,1,3),_AniBsuSuStatusDSFec_Type())
aniBsuSuStatusDSFec.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuStatusDSFec.setStatus(_A)
_AniBsuSuStatusDSRxPower_Type=DisplayString
_AniBsuSuStatusDSRxPower_Object=MibTableColumn
aniBsuSuStatusDSRxPower=_AniBsuSuStatusDSRxPower_Object((1,3,6,1,4,1,4325,3,7,3,2,1,5),_AniBsuSuStatusDSRxPower_Type())
aniBsuSuStatusDSRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuStatusDSRxPower.setStatus(_A)
_AniBsuSuStatusBsuTxPower_Type=Integer32
_AniBsuSuStatusBsuTxPower_Object=MibTableColumn
aniBsuSuStatusBsuTxPower=_AniBsuSuStatusBsuTxPower_Object((1,3,6,1,4,1,4325,3,7,3,2,1,6),_AniBsuSuStatusBsuTxPower_Type())
aniBsuSuStatusBsuTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuStatusBsuTxPower.setStatus(_A)
if mibBuilder.loadTexts:aniBsuSuStatusBsuTxPower.setUnits(_H)
_AniBsuSuLinkStatusTable_Object=MibTable
aniBsuSuLinkStatusTable=_AniBsuSuLinkStatusTable_Object((1,3,6,1,4,1,4325,3,7,3,3))
if mibBuilder.loadTexts:aniBsuSuLinkStatusTable.setStatus(_A)
_AniBsuSuLinkStatusEntry_Object=MibTableRow
aniBsuSuLinkStatusEntry=_AniBsuSuLinkStatusEntry_Object((1,3,6,1,4,1,4325,3,7,3,3,1))
aniBsuSuLinkStatusEntry.setIndexNames((0,_D,_E),(0,_F,_G))
if mibBuilder.loadTexts:aniBsuSuLinkStatusEntry.setStatus(_A)
_AniBsuSuStatusIpAddress_Type=IpAddress
_AniBsuSuStatusIpAddress_Object=MibTableColumn
aniBsuSuStatusIpAddress=_AniBsuSuStatusIpAddress_Object((1,3,6,1,4,1,4325,3,7,3,3,1,1),_AniBsuSuStatusIpAddress_Type())
aniBsuSuStatusIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuStatusIpAddress.setStatus(_A)
_AniBsuSuStatusPropagationDelay_Type=Integer32
_AniBsuSuStatusPropagationDelay_Object=MibTableColumn
aniBsuSuStatusPropagationDelay=_AniBsuSuStatusPropagationDelay_Object((1,3,6,1,4,1,4325,3,7,3,3,1,2),_AniBsuSuStatusPropagationDelay_Type())
aniBsuSuStatusPropagationDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuStatusPropagationDelay.setStatus(_A)
_AniBsuSuStatusDistance_Type=DisplayString
_AniBsuSuStatusDistance_Object=MibTableColumn
aniBsuSuStatusDistance=_AniBsuSuStatusDistance_Object((1,3,6,1,4,1,4325,3,7,3,3,1,3),_AniBsuSuStatusDistance_Type())
aniBsuSuStatusDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuStatusDistance.setStatus(_A)
_AniBsuSuStatusLinkType_Type=DisplayString
_AniBsuSuStatusLinkType_Object=MibTableColumn
aniBsuSuStatusLinkType=_AniBsuSuStatusLinkType_Object((1,3,6,1,4,1,4325,3,7,3,3,1,4),_AniBsuSuStatusLinkType_Type())
aniBsuSuStatusLinkType.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuStatusLinkType.setStatus(_A)
_AniBsuSuStatusPathLossExponent_Type=DisplayString
_AniBsuSuStatusPathLossExponent_Object=MibTableColumn
aniBsuSuStatusPathLossExponent=_AniBsuSuStatusPathLossExponent_Object((1,3,6,1,4,1,4325,3,7,3,3,1,5),_AniBsuSuStatusPathLossExponent_Type())
aniBsuSuStatusPathLossExponent.setMaxAccess(_B)
if mibBuilder.loadTexts:aniBsuSuStatusPathLossExponent.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'aniBsuSuStatus':aniBsuSuStatus,'aniBsuSuUSLinkStatusTable':aniBsuSuUSLinkStatusTable,'aniBsuSuUSLinkStatusEntry':aniBsuSuUSLinkStatusEntry,_G:aniBsuSuStatusMacAddr,'aniBsuSuStatusIpAddr':aniBsuSuStatusIpAddr,'aniBsuSuStatusUSPolarization':aniBsuSuStatusUSPolarization,'aniBsuSuStatusUSModulation':aniBsuSuStatusUSModulation,'aniBsuSuStatusUSFec':aniBsuSuStatusUSFec,'aniBsuSuStatusSuTxPowerAttn':aniBsuSuStatusSuTxPowerAttn,'aniBsuSuStatusUSRxPower':aniBsuSuStatusUSRxPower,'aniBsuSuStatusSuTxPower':aniBsuSuStatusSuTxPower,'aniBsuSuDSLinkStatusTable':aniBsuSuDSLinkStatusTable,'aniBsuSuDSLinkStatusEntry':aniBsuSuDSLinkStatusEntry,'aniBsuSuStatusDSPolarization':aniBsuSuStatusDSPolarization,'aniBsuSuStatusDSModulation':aniBsuSuStatusDSModulation,'aniBsuSuStatusDSFec':aniBsuSuStatusDSFec,'aniBsuSuStatusDSRxPower':aniBsuSuStatusDSRxPower,'aniBsuSuStatusBsuTxPower':aniBsuSuStatusBsuTxPower,'aniBsuSuLinkStatusTable':aniBsuSuLinkStatusTable,'aniBsuSuLinkStatusEntry':aniBsuSuLinkStatusEntry,'aniBsuSuStatusIpAddress':aniBsuSuStatusIpAddress,'aniBsuSuStatusPropagationDelay':aniBsuSuStatusPropagationDelay,'aniBsuSuStatusDistance':aniBsuSuStatusDistance,'aniBsuSuStatusLinkType':aniBsuSuStatusLinkType,'aniBsuSuStatusPathLossExponent':aniBsuSuStatusPathLossExponent})