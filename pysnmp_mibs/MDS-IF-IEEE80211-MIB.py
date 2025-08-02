_o='mIfDot11StatusApGroup'
_n='mIfDot11StatusStationGroup'
_m='mIfDot11StatusCommonGroup'
_l='mIfDot11ApClientTxretries'
_k='mIfDot11ApClientTxfailed'
_j='mIfDot11ApClientTxpackets'
_i='mIfDot11ApClientTxbytes'
_h='mIfDot11ApClientTxbitrate'
_g='mIfDot11ApClientRxpackets'
_f='mIfDot11ApClientRxbytes'
_e='mIfDot11ApClientInactive'
_d='mIfDot11ApClientAuthorized'
_c='mIfDot11ApClientAuthenticated'
_b='mIfDot11ApClientRssi'
_a='mIfDot11StationTxretries'
_Z='mIfDot11StationTxfailed'
_Y='mIfDot11StationTxpackets'
_X='mIfDot11StationTxbytes'
_W='mIfDot11StationTxbitrate'
_V='mIfDot11StationRxpackets'
_U='mIfDot11StationRxbytes'
_T='mIfDot11StationInactive'
_S='mIfDot11StationAuthorized'
_R='mIfDot11StationAuthenticated'
_Q='mIfDot11StationBssid'
_P='mIfDot11StationRssi'
_O='mIfDot11StationSsid'
_N='mIfDot11ModemType'
_M='mIfDot11Channel'
_L='mIfDot11TxPower'
_K='mIfDot11Mode'
_J='mIfDot11SerialNumber'
_I='unknown'
_H='mIfDot11ApClientMac'
_G='Integer32'
_F='mIfDot11ApSsid'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='MDS-IF-IEEE80211-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
mdsInterfaces,=mibBuilder.importSymbols('MDS-ORBIT-SMI-MIB','mdsInterfaces')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
mdsIfDot11MIB=ModuleIdentity((1,3,6,1,4,1,4130,10,2,2))
if mibBuilder.loadTexts:mdsIfDot11MIB.setRevisions(('2018-05-16 00:00','2014-10-20 00:00','2013-04-26 00:00'))
class Byte(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,127))
class UnsignedByte(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class UnsignedShort(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class Ssid(TextualConvention,OctetString):status=_A;displayHint='32a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
class MacString(TextualConvention,OctetString):status=_A;displayHint='20a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_MIfDot11MIBObjects_ObjectIdentity=ObjectIdentity
mIfDot11MIBObjects=_MIfDot11MIBObjects_ObjectIdentity((1,3,6,1,4,1,4130,10,2,2,1))
_MIfDot11Config_ObjectIdentity=ObjectIdentity
mIfDot11Config=_MIfDot11Config_ObjectIdentity((1,3,6,1,4,1,4130,10,2,2,1,1))
_MIfDot11Status_ObjectIdentity=ObjectIdentity
mIfDot11Status=_MIfDot11Status_ObjectIdentity((1,3,6,1,4,1,4130,10,2,2,1,2))
_MIfDot11StatusTable_Object=MibTable
mIfDot11StatusTable=_MIfDot11StatusTable_Object((1,3,6,1,4,1,4130,10,2,2,1,2,1))
if mibBuilder.loadTexts:mIfDot11StatusTable.setStatus(_A)
_MIfDot11StatusEntry_Object=MibTableRow
mIfDot11StatusEntry=_MIfDot11StatusEntry_Object((1,3,6,1,4,1,4130,10,2,2,1,2,1,1))
mIfDot11StatusEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:mIfDot11StatusEntry.setStatus(_A)
_MIfDot11SerialNumber_Type=DisplayString
_MIfDot11SerialNumber_Object=MibTableColumn
mIfDot11SerialNumber=_MIfDot11SerialNumber_Object((1,3,6,1,4,1,4130,10,2,2,1,2,1,1,1),_MIfDot11SerialNumber_Type())
mIfDot11SerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11SerialNumber.setStatus(_A)
class _MIfDot11Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_I,0),('station',1),('accessPoint',2),('accessPointStation',3)))
_MIfDot11Mode_Type.__name__=_G
_MIfDot11Mode_Object=MibTableColumn
mIfDot11Mode=_MIfDot11Mode_Object((1,3,6,1,4,1,4130,10,2,2,1,2,1,1,2),_MIfDot11Mode_Type())
mIfDot11Mode.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11Mode.setStatus(_A)
_MIfDot11TxPower_Type=UnsignedByte
_MIfDot11TxPower_Object=MibTableColumn
mIfDot11TxPower=_MIfDot11TxPower_Object((1,3,6,1,4,1,4130,10,2,2,1,2,1,1,3),_MIfDot11TxPower_Type())
mIfDot11TxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11TxPower.setStatus(_A)
_MIfDot11Channel_Type=UnsignedByte
_MIfDot11Channel_Object=MibTableColumn
mIfDot11Channel=_MIfDot11Channel_Object((1,3,6,1,4,1,4130,10,2,2,1,2,1,1,4),_MIfDot11Channel_Type())
mIfDot11Channel.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11Channel.setStatus(_A)
_MIfDot11StationSsid_Type=Ssid
_MIfDot11StationSsid_Object=MibTableColumn
mIfDot11StationSsid=_MIfDot11StationSsid_Object((1,3,6,1,4,1,4130,10,2,2,1,2,1,1,5),_MIfDot11StationSsid_Type())
mIfDot11StationSsid.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11StationSsid.setStatus(_A)
_MIfDot11StationBssid_Type=MacString
_MIfDot11StationBssid_Object=MibTableColumn
mIfDot11StationBssid=_MIfDot11StationBssid_Object((1,3,6,1,4,1,4130,10,2,2,1,2,1,1,6),_MIfDot11StationBssid_Type())
mIfDot11StationBssid.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11StationBssid.setStatus(_A)
_MIfDot11StationRssi_Type=Byte
_MIfDot11StationRssi_Object=MibTableColumn
mIfDot11StationRssi=_MIfDot11StationRssi_Object((1,3,6,1,4,1,4130,10,2,2,1,2,1,1,7),_MIfDot11StationRssi_Type())
mIfDot11StationRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11StationRssi.setStatus(_A)
_MIfDot11StationAuthenticated_Type=TruthValue
_MIfDot11StationAuthenticated_Object=MibTableColumn
mIfDot11StationAuthenticated=_MIfDot11StationAuthenticated_Object((1,3,6,1,4,1,4130,10,2,2,1,2,1,1,8),_MIfDot11StationAuthenticated_Type())
mIfDot11StationAuthenticated.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11StationAuthenticated.setStatus(_A)
_MIfDot11StationAuthorized_Type=TruthValue
_MIfDot11StationAuthorized_Object=MibTableColumn
mIfDot11StationAuthorized=_MIfDot11StationAuthorized_Object((1,3,6,1,4,1,4130,10,2,2,1,2,1,1,9),_MIfDot11StationAuthorized_Type())
mIfDot11StationAuthorized.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11StationAuthorized.setStatus(_A)
_MIfDot11StationInactive_Type=Unsigned32
_MIfDot11StationInactive_Object=MibTableColumn
mIfDot11StationInactive=_MIfDot11StationInactive_Object((1,3,6,1,4,1,4130,10,2,2,1,2,1,1,10),_MIfDot11StationInactive_Type())
mIfDot11StationInactive.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11StationInactive.setStatus(_A)
_MIfDot11StationRxbytes_Type=Unsigned32
_MIfDot11StationRxbytes_Object=MibTableColumn
mIfDot11StationRxbytes=_MIfDot11StationRxbytes_Object((1,3,6,1,4,1,4130,10,2,2,1,2,1,1,11),_MIfDot11StationRxbytes_Type())
mIfDot11StationRxbytes.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11StationRxbytes.setStatus(_A)
_MIfDot11StationRxpackets_Type=Unsigned32
_MIfDot11StationRxpackets_Object=MibTableColumn
mIfDot11StationRxpackets=_MIfDot11StationRxpackets_Object((1,3,6,1,4,1,4130,10,2,2,1,2,1,1,12),_MIfDot11StationRxpackets_Type())
mIfDot11StationRxpackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11StationRxpackets.setStatus(_A)
_MIfDot11StationTxbitrate_Type=UnsignedShort
_MIfDot11StationTxbitrate_Object=MibTableColumn
mIfDot11StationTxbitrate=_MIfDot11StationTxbitrate_Object((1,3,6,1,4,1,4130,10,2,2,1,2,1,1,13),_MIfDot11StationTxbitrate_Type())
mIfDot11StationTxbitrate.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11StationTxbitrate.setStatus(_A)
_MIfDot11StationTxbytes_Type=Unsigned32
_MIfDot11StationTxbytes_Object=MibTableColumn
mIfDot11StationTxbytes=_MIfDot11StationTxbytes_Object((1,3,6,1,4,1,4130,10,2,2,1,2,1,1,14),_MIfDot11StationTxbytes_Type())
mIfDot11StationTxbytes.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11StationTxbytes.setStatus(_A)
_MIfDot11StationTxpackets_Type=Unsigned32
_MIfDot11StationTxpackets_Object=MibTableColumn
mIfDot11StationTxpackets=_MIfDot11StationTxpackets_Object((1,3,6,1,4,1,4130,10,2,2,1,2,1,1,15),_MIfDot11StationTxpackets_Type())
mIfDot11StationTxpackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11StationTxpackets.setStatus(_A)
_MIfDot11StationTxfailed_Type=Unsigned32
_MIfDot11StationTxfailed_Object=MibTableColumn
mIfDot11StationTxfailed=_MIfDot11StationTxfailed_Object((1,3,6,1,4,1,4130,10,2,2,1,2,1,1,16),_MIfDot11StationTxfailed_Type())
mIfDot11StationTxfailed.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11StationTxfailed.setStatus(_A)
_MIfDot11StationTxretries_Type=Unsigned32
_MIfDot11StationTxretries_Object=MibTableColumn
mIfDot11StationTxretries=_MIfDot11StationTxretries_Object((1,3,6,1,4,1,4130,10,2,2,1,2,1,1,17),_MIfDot11StationTxretries_Type())
mIfDot11StationTxretries.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11StationTxretries.setStatus(_A)
class _MIfDot11ModemType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),('w51',1),('w52',2)))
_MIfDot11ModemType_Type.__name__=_G
_MIfDot11ModemType_Object=MibTableColumn
mIfDot11ModemType=_MIfDot11ModemType_Object((1,3,6,1,4,1,4130,10,2,2,1,2,1,1,18),_MIfDot11ModemType_Type())
mIfDot11ModemType.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11ModemType.setStatus(_A)
_MIfDot11StatusApTable_Object=MibTable
mIfDot11StatusApTable=_MIfDot11StatusApTable_Object((1,3,6,1,4,1,4130,10,2,2,1,2,2))
if mibBuilder.loadTexts:mIfDot11StatusApTable.setStatus(_A)
_MIfDot11StatusApEntry_Object=MibTableRow
mIfDot11StatusApEntry=_MIfDot11StatusApEntry_Object((1,3,6,1,4,1,4130,10,2,2,1,2,2,1))
mIfDot11StatusApEntry.setIndexNames((0,_D,_E),(0,_B,_F))
if mibBuilder.loadTexts:mIfDot11StatusApEntry.setStatus(_A)
_MIfDot11ApSsid_Type=Ssid
_MIfDot11ApSsid_Object=MibTableColumn
mIfDot11ApSsid=_MIfDot11ApSsid_Object((1,3,6,1,4,1,4130,10,2,2,1,2,2,1,1),_MIfDot11ApSsid_Type())
mIfDot11ApSsid.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11ApSsid.setStatus(_A)
_MIfDot11StatusApClientTable_Object=MibTable
mIfDot11StatusApClientTable=_MIfDot11StatusApClientTable_Object((1,3,6,1,4,1,4130,10,2,2,1,2,3))
if mibBuilder.loadTexts:mIfDot11StatusApClientTable.setStatus(_A)
_MIfDot11StatusApClientEntry_Object=MibTableRow
mIfDot11StatusApClientEntry=_MIfDot11StatusApClientEntry_Object((1,3,6,1,4,1,4130,10,2,2,1,2,3,1))
mIfDot11StatusApClientEntry.setIndexNames((0,_D,_E),(0,_B,_F),(0,_B,_H))
if mibBuilder.loadTexts:mIfDot11StatusApClientEntry.setStatus(_A)
_MIfDot11ApClientMac_Type=MacString
_MIfDot11ApClientMac_Object=MibTableColumn
mIfDot11ApClientMac=_MIfDot11ApClientMac_Object((1,3,6,1,4,1,4130,10,2,2,1,2,3,1,1),_MIfDot11ApClientMac_Type())
mIfDot11ApClientMac.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11ApClientMac.setStatus(_A)
_MIfDot11ApClientRssi_Type=Byte
_MIfDot11ApClientRssi_Object=MibTableColumn
mIfDot11ApClientRssi=_MIfDot11ApClientRssi_Object((1,3,6,1,4,1,4130,10,2,2,1,2,3,1,2),_MIfDot11ApClientRssi_Type())
mIfDot11ApClientRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11ApClientRssi.setStatus(_A)
_MIfDot11ApClientAuthenticated_Type=TruthValue
_MIfDot11ApClientAuthenticated_Object=MibTableColumn
mIfDot11ApClientAuthenticated=_MIfDot11ApClientAuthenticated_Object((1,3,6,1,4,1,4130,10,2,2,1,2,3,1,3),_MIfDot11ApClientAuthenticated_Type())
mIfDot11ApClientAuthenticated.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11ApClientAuthenticated.setStatus(_A)
_MIfDot11ApClientAuthorized_Type=TruthValue
_MIfDot11ApClientAuthorized_Object=MibTableColumn
mIfDot11ApClientAuthorized=_MIfDot11ApClientAuthorized_Object((1,3,6,1,4,1,4130,10,2,2,1,2,3,1,4),_MIfDot11ApClientAuthorized_Type())
mIfDot11ApClientAuthorized.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11ApClientAuthorized.setStatus(_A)
_MIfDot11ApClientInactive_Type=Unsigned32
_MIfDot11ApClientInactive_Object=MibTableColumn
mIfDot11ApClientInactive=_MIfDot11ApClientInactive_Object((1,3,6,1,4,1,4130,10,2,2,1,2,3,1,5),_MIfDot11ApClientInactive_Type())
mIfDot11ApClientInactive.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11ApClientInactive.setStatus(_A)
_MIfDot11ApClientRxbytes_Type=Unsigned32
_MIfDot11ApClientRxbytes_Object=MibTableColumn
mIfDot11ApClientRxbytes=_MIfDot11ApClientRxbytes_Object((1,3,6,1,4,1,4130,10,2,2,1,2,3,1,6),_MIfDot11ApClientRxbytes_Type())
mIfDot11ApClientRxbytes.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11ApClientRxbytes.setStatus(_A)
_MIfDot11ApClientRxpackets_Type=Unsigned32
_MIfDot11ApClientRxpackets_Object=MibTableColumn
mIfDot11ApClientRxpackets=_MIfDot11ApClientRxpackets_Object((1,3,6,1,4,1,4130,10,2,2,1,2,3,1,7),_MIfDot11ApClientRxpackets_Type())
mIfDot11ApClientRxpackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11ApClientRxpackets.setStatus(_A)
_MIfDot11ApClientTxbitrate_Type=UnsignedShort
_MIfDot11ApClientTxbitrate_Object=MibTableColumn
mIfDot11ApClientTxbitrate=_MIfDot11ApClientTxbitrate_Object((1,3,6,1,4,1,4130,10,2,2,1,2,3,1,8),_MIfDot11ApClientTxbitrate_Type())
mIfDot11ApClientTxbitrate.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11ApClientTxbitrate.setStatus(_A)
_MIfDot11ApClientTxbytes_Type=Unsigned32
_MIfDot11ApClientTxbytes_Object=MibTableColumn
mIfDot11ApClientTxbytes=_MIfDot11ApClientTxbytes_Object((1,3,6,1,4,1,4130,10,2,2,1,2,3,1,9),_MIfDot11ApClientTxbytes_Type())
mIfDot11ApClientTxbytes.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11ApClientTxbytes.setStatus(_A)
_MIfDot11ApClientTxpackets_Type=Unsigned32
_MIfDot11ApClientTxpackets_Object=MibTableColumn
mIfDot11ApClientTxpackets=_MIfDot11ApClientTxpackets_Object((1,3,6,1,4,1,4130,10,2,2,1,2,3,1,10),_MIfDot11ApClientTxpackets_Type())
mIfDot11ApClientTxpackets.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11ApClientTxpackets.setStatus(_A)
_MIfDot11ApClientTxfailed_Type=Unsigned32
_MIfDot11ApClientTxfailed_Object=MibTableColumn
mIfDot11ApClientTxfailed=_MIfDot11ApClientTxfailed_Object((1,3,6,1,4,1,4130,10,2,2,1,2,3,1,11),_MIfDot11ApClientTxfailed_Type())
mIfDot11ApClientTxfailed.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11ApClientTxfailed.setStatus(_A)
_MIfDot11ApClientTxretries_Type=Unsigned32
_MIfDot11ApClientTxretries_Object=MibTableColumn
mIfDot11ApClientTxretries=_MIfDot11ApClientTxretries_Object((1,3,6,1,4,1,4130,10,2,2,1,2,3,1,12),_MIfDot11ApClientTxretries_Type())
mIfDot11ApClientTxretries.setMaxAccess(_C)
if mibBuilder.loadTexts:mIfDot11ApClientTxretries.setStatus(_A)
_MdsIfDot11MIBConformance_ObjectIdentity=ObjectIdentity
mdsIfDot11MIBConformance=_MdsIfDot11MIBConformance_ObjectIdentity((1,3,6,1,4,1,4130,10,2,2,3))
_MdsIfDot11MIBCompliances_ObjectIdentity=ObjectIdentity
mdsIfDot11MIBCompliances=_MdsIfDot11MIBCompliances_ObjectIdentity((1,3,6,1,4,1,4130,10,2,2,3,1))
_MdsIfDot11MIBGroups_ObjectIdentity=ObjectIdentity
mdsIfDot11MIBGroups=_MdsIfDot11MIBGroups_ObjectIdentity((1,3,6,1,4,1,4130,10,2,2,3,2))
mIfDot11StatusCommonGroup=ObjectGroup((1,3,6,1,4,1,4130,10,2,2,3,2,1))
mIfDot11StatusCommonGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:mIfDot11StatusCommonGroup.setStatus(_A)
mIfDot11StatusStationGroup=ObjectGroup((1,3,6,1,4,1,4130,10,2,2,3,2,2))
mIfDot11StatusStationGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:mIfDot11StatusStationGroup.setStatus(_A)
mIfDot11StatusApGroup=ObjectGroup((1,3,6,1,4,1,4130,10,2,2,3,2,3))
mIfDot11StatusApGroup.setObjects(*((_B,_F),(_B,_H),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:mIfDot11StatusApGroup.setStatus(_A)
mIfDot11Compliance=ModuleCompliance((1,3,6,1,4,1,4130,10,2,2,3,1,1))
mIfDot11Compliance.setObjects(*((_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:mIfDot11Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Byte':Byte,'UnsignedByte':UnsignedByte,'UnsignedShort':UnsignedShort,'Ssid':Ssid,'MacString':MacString,'mdsIfDot11MIB':mdsIfDot11MIB,'mIfDot11MIBObjects':mIfDot11MIBObjects,'mIfDot11Config':mIfDot11Config,'mIfDot11Status':mIfDot11Status,'mIfDot11StatusTable':mIfDot11StatusTable,'mIfDot11StatusEntry':mIfDot11StatusEntry,_J:mIfDot11SerialNumber,_K:mIfDot11Mode,_L:mIfDot11TxPower,_M:mIfDot11Channel,_O:mIfDot11StationSsid,_Q:mIfDot11StationBssid,_P:mIfDot11StationRssi,_R:mIfDot11StationAuthenticated,_S:mIfDot11StationAuthorized,_T:mIfDot11StationInactive,_U:mIfDot11StationRxbytes,_V:mIfDot11StationRxpackets,_W:mIfDot11StationTxbitrate,_X:mIfDot11StationTxbytes,_Y:mIfDot11StationTxpackets,_Z:mIfDot11StationTxfailed,_a:mIfDot11StationTxretries,_N:mIfDot11ModemType,'mIfDot11StatusApTable':mIfDot11StatusApTable,'mIfDot11StatusApEntry':mIfDot11StatusApEntry,_F:mIfDot11ApSsid,'mIfDot11StatusApClientTable':mIfDot11StatusApClientTable,'mIfDot11StatusApClientEntry':mIfDot11StatusApClientEntry,_H:mIfDot11ApClientMac,_b:mIfDot11ApClientRssi,_c:mIfDot11ApClientAuthenticated,_d:mIfDot11ApClientAuthorized,_e:mIfDot11ApClientInactive,_f:mIfDot11ApClientRxbytes,_g:mIfDot11ApClientRxpackets,_h:mIfDot11ApClientTxbitrate,_i:mIfDot11ApClientTxbytes,_j:mIfDot11ApClientTxpackets,_k:mIfDot11ApClientTxfailed,_l:mIfDot11ApClientTxretries,'mdsIfDot11MIBConformance':mdsIfDot11MIBConformance,'mdsIfDot11MIBCompliances':mdsIfDot11MIBCompliances,'mIfDot11Compliance':mIfDot11Compliance,'mdsIfDot11MIBGroups':mdsIfDot11MIBGroups,_m:mIfDot11StatusCommonGroup,_n:mIfDot11StatusStationGroup,_o:mIfDot11StatusApGroup})