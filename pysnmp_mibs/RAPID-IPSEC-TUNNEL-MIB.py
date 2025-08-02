_J='Kbytes'
_I='ip-addr-range'
_H='ip-addr-subnet'
_G='ip-addr-single'
_F='rsIpsecTunnelID'
_E='RAPID-IPSEC-TUNNEL-MIB'
_D='unknown'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rapidstream,=mibBuilder.importSymbols('RAPID-MIB','rapidstream')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
rsInfoModule=ModuleIdentity((1,3,6,1,4,1,4355,6))
if mibBuilder.loadTexts:rsInfoModule.setRevisions(('2001-04-20 12:00','2002-11-01 12:00'))
_RsIpsecTunnelMIB_ObjectIdentity=ObjectIdentity
rsIpsecTunnelMIB=_RsIpsecTunnelMIB_ObjectIdentity((1,3,6,1,4,1,4355,6,5))
if mibBuilder.loadTexts:rsIpsecTunnelMIB.setStatus(_A)
_RsIpsecTunnel_ObjectIdentity=ObjectIdentity
rsIpsecTunnel=_RsIpsecTunnel_ObjectIdentity((1,3,6,1,4,1,4355,6,5,1))
if mibBuilder.loadTexts:rsIpsecTunnel.setStatus(_A)
_RsIpsecTunnelNum_Type=Unsigned32
_RsIpsecTunnelNum_Object=MibScalar
rsIpsecTunnelNum=_RsIpsecTunnelNum_Object((1,3,6,1,4,1,4355,6,5,1,1),_RsIpsecTunnelNum_Type())
rsIpsecTunnelNum.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelNum.setStatus(_A)
_RsIpsecTunnelTable_Object=MibTable
rsIpsecTunnelTable=_RsIpsecTunnelTable_Object((1,3,6,1,4,1,4355,6,5,1,2))
if mibBuilder.loadTexts:rsIpsecTunnelTable.setStatus(_A)
_RsIpsecTunnelEntry_Object=MibTableRow
rsIpsecTunnelEntry=_RsIpsecTunnelEntry_Object((1,3,6,1,4,1,4355,6,5,1,2,1))
rsIpsecTunnelEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:rsIpsecTunnelEntry.setStatus(_A)
_RsIpsecTunnelID_Type=Integer32
_RsIpsecTunnelID_Object=MibTableColumn
rsIpsecTunnelID=_RsIpsecTunnelID_Object((1,3,6,1,4,1,4355,6,5,1,2,1,1),_RsIpsecTunnelID_Type())
rsIpsecTunnelID.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelID.setStatus(_A)
_RsIpsecTunnelLocalAddr_Type=IpAddress
_RsIpsecTunnelLocalAddr_Object=MibTableColumn
rsIpsecTunnelLocalAddr=_RsIpsecTunnelLocalAddr_Object((1,3,6,1,4,1,4355,6,5,1,2,1,2),_RsIpsecTunnelLocalAddr_Type())
rsIpsecTunnelLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelLocalAddr.setStatus(_A)
_RsIpsecTunnelPeerAddr_Type=IpAddress
_RsIpsecTunnelPeerAddr_Object=MibTableColumn
rsIpsecTunnelPeerAddr=_RsIpsecTunnelPeerAddr_Object((1,3,6,1,4,1,4355,6,5,1,2,1,3),_RsIpsecTunnelPeerAddr_Type())
rsIpsecTunnelPeerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelPeerAddr.setStatus(_A)
_RsIpsecTunnelInSpi_Type=Integer32
_RsIpsecTunnelInSpi_Object=MibTableColumn
rsIpsecTunnelInSpi=_RsIpsecTunnelInSpi_Object((1,3,6,1,4,1,4355,6,5,1,2,1,4),_RsIpsecTunnelInSpi_Type())
rsIpsecTunnelInSpi.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelInSpi.setStatus(_A)
_RsIpsecTunnelOutSpi_Type=Integer32
_RsIpsecTunnelOutSpi_Object=MibTableColumn
rsIpsecTunnelOutSpi=_RsIpsecTunnelOutSpi_Object((1,3,6,1,4,1,4355,6,5,1,2,1,5),_RsIpsecTunnelOutSpi_Type())
rsIpsecTunnelOutSpi.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelOutSpi.setStatus(_A)
_RsIpsecTunnelCreateTime_Type=DateAndTime
_RsIpsecTunnelCreateTime_Object=MibTableColumn
rsIpsecTunnelCreateTime=_RsIpsecTunnelCreateTime_Object((1,3,6,1,4,1,4355,6,5,1,2,1,6),_RsIpsecTunnelCreateTime_Type())
rsIpsecTunnelCreateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelCreateTime.setStatus(_A)
_RsIpsecTunnelDeviceID_Type=Unsigned32
_RsIpsecTunnelDeviceID_Object=MibTableColumn
rsIpsecTunnelDeviceID=_RsIpsecTunnelDeviceID_Object((1,3,6,1,4,1,4355,6,5,1,2,1,7),_RsIpsecTunnelDeviceID_Type())
rsIpsecTunnelDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelDeviceID.setStatus(_A)
class _RsIpsecTunnelEspEncryptAlg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3)));namedValues=NamedValues(*((_D,0),('des',2),('three-des',3)))
_RsIpsecTunnelEspEncryptAlg_Type.__name__=_C
_RsIpsecTunnelEspEncryptAlg_Object=MibTableColumn
rsIpsecTunnelEspEncryptAlg=_RsIpsecTunnelEspEncryptAlg_Object((1,3,6,1,4,1,4355,6,5,1,2,1,8),_RsIpsecTunnelEspEncryptAlg_Type())
rsIpsecTunnelEspEncryptAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelEspEncryptAlg.setStatus(_A)
class _RsIpsecTunnelEspAuthAlg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3)));namedValues=NamedValues(*((_D,0),('md5',2),('sha',3)))
_RsIpsecTunnelEspAuthAlg_Type.__name__=_C
_RsIpsecTunnelEspAuthAlg_Object=MibTableColumn
rsIpsecTunnelEspAuthAlg=_RsIpsecTunnelEspAuthAlg_Object((1,3,6,1,4,1,4355,6,5,1,2,1,9),_RsIpsecTunnelEspAuthAlg_Type())
rsIpsecTunnelEspAuthAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelEspAuthAlg.setStatus(_A)
class _RsIpsecTunnelAhAuthAlg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3)));namedValues=NamedValues(*((_D,0),('md5',2),('sha',3)))
_RsIpsecTunnelAhAuthAlg_Type.__name__=_C
_RsIpsecTunnelAhAuthAlg_Object=MibTableColumn
rsIpsecTunnelAhAuthAlg=_RsIpsecTunnelAhAuthAlg_Object((1,3,6,1,4,1,4355,6,5,1,2,1,10),_RsIpsecTunnelAhAuthAlg_Type())
rsIpsecTunnelAhAuthAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelAhAuthAlg.setStatus(_A)
class _RsIpsecTunnelMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),('tunnel',1),('transport',2)))
_RsIpsecTunnelMode_Type.__name__=_C
_RsIpsecTunnelMode_Object=MibTableColumn
rsIpsecTunnelMode=_RsIpsecTunnelMode_Object((1,3,6,1,4,1,4355,6,5,1,2,1,11),_RsIpsecTunnelMode_Type())
rsIpsecTunnelMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelMode.setStatus(_A)
class _RsIpsecTunnelKeyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),('manual',1),('auto-ike',2),('other',3)))
_RsIpsecTunnelKeyMode_Type.__name__=_C
_RsIpsecTunnelKeyMode_Object=MibTableColumn
rsIpsecTunnelKeyMode=_RsIpsecTunnelKeyMode_Object((1,3,6,1,4,1,4355,6,5,1,2,1,12),_RsIpsecTunnelKeyMode_Type())
rsIpsecTunnelKeyMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelKeyMode.setStatus(_A)
_RsIpsecTunnelLifeTime_Type=TimeTicks
_RsIpsecTunnelLifeTime_Object=MibTableColumn
rsIpsecTunnelLifeTime=_RsIpsecTunnelLifeTime_Object((1,3,6,1,4,1,4355,6,5,1,2,1,13),_RsIpsecTunnelLifeTime_Type())
rsIpsecTunnelLifeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelLifeTime.setStatus(_A)
_RsIpsecTunnelLifeLength_Type=Counter32
_RsIpsecTunnelLifeLength_Object=MibTableColumn
rsIpsecTunnelLifeLength=_RsIpsecTunnelLifeLength_Object((1,3,6,1,4,1,4355,6,5,1,2,1,14),_RsIpsecTunnelLifeLength_Type())
rsIpsecTunnelLifeLength.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelLifeLength.setStatus(_A)
_RsIpsecTunnelInSaBytes_Type=Counter32
_RsIpsecTunnelInSaBytes_Object=MibTableColumn
rsIpsecTunnelInSaBytes=_RsIpsecTunnelInSaBytes_Object((1,3,6,1,4,1,4355,6,5,1,2,1,15),_RsIpsecTunnelInSaBytes_Type())
rsIpsecTunnelInSaBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelInSaBytes.setStatus(_A)
_RsIpsecTunnelOutSaBytes_Type=Counter32
_RsIpsecTunnelOutSaBytes_Object=MibTableColumn
rsIpsecTunnelOutSaBytes=_RsIpsecTunnelOutSaBytes_Object((1,3,6,1,4,1,4355,6,5,1,2,1,16),_RsIpsecTunnelOutSaBytes_Type())
rsIpsecTunnelOutSaBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelOutSaBytes.setStatus(_A)
_RsIpsecTunnelAccSecs_Type=Counter32
_RsIpsecTunnelAccSecs_Object=MibTableColumn
rsIpsecTunnelAccSecs=_RsIpsecTunnelAccSecs_Object((1,3,6,1,4,1,4355,6,5,1,2,1,17),_RsIpsecTunnelAccSecs_Type())
rsIpsecTunnelAccSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelAccSecs.setStatus(_A)
class _RsIpsecTunnelSelectorProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,6,8,12,17,22,29,41,43,44,46,47,50,51,58,59,60,92,98,103,255)));namedValues=NamedValues(*(('any',0),('icmp',1),('igmp',2),('ipip',4),('tcp',6),('egp',8),('pup',12),('udp',17),('idp',22),('tp',29),('ipv6',41),('ipv6-routing',43),('ipv6-fragmentation',44),('rsvp',46),('gre',47),('esp',50),('ah',51),('icmpv6',58),('none',59),('dstopts',60),('mtp',92),('encap',98),('pim',103),('raw',255)))
_RsIpsecTunnelSelectorProtocol_Type.__name__=_C
_RsIpsecTunnelSelectorProtocol_Object=MibTableColumn
rsIpsecTunnelSelectorProtocol=_RsIpsecTunnelSelectorProtocol_Object((1,3,6,1,4,1,4355,6,5,1,2,1,18),_RsIpsecTunnelSelectorProtocol_Type())
rsIpsecTunnelSelectorProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelSelectorProtocol.setStatus(_A)
class _RsIpsecTunnelSelectorRemoteIPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_RsIpsecTunnelSelectorRemoteIPType_Type.__name__=_C
_RsIpsecTunnelSelectorRemoteIPType_Object=MibTableColumn
rsIpsecTunnelSelectorRemoteIPType=_RsIpsecTunnelSelectorRemoteIPType_Object((1,3,6,1,4,1,4355,6,5,1,2,1,19),_RsIpsecTunnelSelectorRemoteIPType_Type())
rsIpsecTunnelSelectorRemoteIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelSelectorRemoteIPType.setStatus(_A)
_RsIpsecTunnelSelectorRemoteIPOne_Type=IpAddress
_RsIpsecTunnelSelectorRemoteIPOne_Object=MibTableColumn
rsIpsecTunnelSelectorRemoteIPOne=_RsIpsecTunnelSelectorRemoteIPOne_Object((1,3,6,1,4,1,4355,6,5,1,2,1,20),_RsIpsecTunnelSelectorRemoteIPOne_Type())
rsIpsecTunnelSelectorRemoteIPOne.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelSelectorRemoteIPOne.setStatus(_A)
_RsIpsecTunnelSelectorRemoteIPTwo_Type=IpAddress
_RsIpsecTunnelSelectorRemoteIPTwo_Object=MibTableColumn
rsIpsecTunnelSelectorRemoteIPTwo=_RsIpsecTunnelSelectorRemoteIPTwo_Object((1,3,6,1,4,1,4355,6,5,1,2,1,21),_RsIpsecTunnelSelectorRemoteIPTwo_Type())
rsIpsecTunnelSelectorRemoteIPTwo.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelSelectorRemoteIPTwo.setStatus(_A)
class _RsIpsecTunnelSelectorRemotePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RsIpsecTunnelSelectorRemotePort_Type.__name__=_C
_RsIpsecTunnelSelectorRemotePort_Object=MibTableColumn
rsIpsecTunnelSelectorRemotePort=_RsIpsecTunnelSelectorRemotePort_Object((1,3,6,1,4,1,4355,6,5,1,2,1,22),_RsIpsecTunnelSelectorRemotePort_Type())
rsIpsecTunnelSelectorRemotePort.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelSelectorRemotePort.setStatus(_A)
class _RsIpsecTunnelSelectorLocalIPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_RsIpsecTunnelSelectorLocalIPType_Type.__name__=_C
_RsIpsecTunnelSelectorLocalIPType_Object=MibTableColumn
rsIpsecTunnelSelectorLocalIPType=_RsIpsecTunnelSelectorLocalIPType_Object((1,3,6,1,4,1,4355,6,5,1,2,1,23),_RsIpsecTunnelSelectorLocalIPType_Type())
rsIpsecTunnelSelectorLocalIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelSelectorLocalIPType.setStatus(_A)
_RsIpsecTunnelSelectorLocalIPOne_Type=IpAddress
_RsIpsecTunnelSelectorLocalIPOne_Object=MibTableColumn
rsIpsecTunnelSelectorLocalIPOne=_RsIpsecTunnelSelectorLocalIPOne_Object((1,3,6,1,4,1,4355,6,5,1,2,1,24),_RsIpsecTunnelSelectorLocalIPOne_Type())
rsIpsecTunnelSelectorLocalIPOne.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelSelectorLocalIPOne.setStatus(_A)
_RsIpsecTunnelSelectorLocalIPTwo_Type=IpAddress
_RsIpsecTunnelSelectorLocalIPTwo_Object=MibTableColumn
rsIpsecTunnelSelectorLocalIPTwo=_RsIpsecTunnelSelectorLocalIPTwo_Object((1,3,6,1,4,1,4355,6,5,1,2,1,25),_RsIpsecTunnelSelectorLocalIPTwo_Type())
rsIpsecTunnelSelectorLocalIPTwo.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelSelectorLocalIPTwo.setStatus(_A)
class _RsIpsecTunnelSelectorLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RsIpsecTunnelSelectorLocalPort_Type.__name__=_C
_RsIpsecTunnelSelectorLocalPort_Object=MibTableColumn
rsIpsecTunnelSelectorLocalPort=_RsIpsecTunnelSelectorLocalPort_Object((1,3,6,1,4,1,4355,6,5,1,2,1,26),_RsIpsecTunnelSelectorLocalPort_Type())
rsIpsecTunnelSelectorLocalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelSelectorLocalPort.setStatus(_A)
_RsIpsecTunnelNumRekey_Type=Counter32
_RsIpsecTunnelNumRekey_Object=MibTableColumn
rsIpsecTunnelNumRekey=_RsIpsecTunnelNumRekey_Object((1,3,6,1,4,1,4355,6,5,1,2,1,27),_RsIpsecTunnelNumRekey_Type())
rsIpsecTunnelNumRekey.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelNumRekey.setStatus(_A)
_RsIpsecTunnelInKbytes_Type=Counter32
_RsIpsecTunnelInKbytes_Object=MibTableColumn
rsIpsecTunnelInKbytes=_RsIpsecTunnelInKbytes_Object((1,3,6,1,4,1,4355,6,5,1,2,1,28),_RsIpsecTunnelInKbytes_Type())
rsIpsecTunnelInKbytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelInKbytes.setStatus(_A)
if mibBuilder.loadTexts:rsIpsecTunnelInKbytes.setUnits(_J)
_RsIpsecTunnelOutKbytes_Type=Counter32
_RsIpsecTunnelOutKbytes_Object=MibTableColumn
rsIpsecTunnelOutKbytes=_RsIpsecTunnelOutKbytes_Object((1,3,6,1,4,1,4355,6,5,1,2,1,29),_RsIpsecTunnelOutKbytes_Type())
rsIpsecTunnelOutKbytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelOutKbytes.setStatus(_A)
if mibBuilder.loadTexts:rsIpsecTunnelOutKbytes.setUnits(_J)
_RsIpsecTunnelInPackets_Type=Counter32
_RsIpsecTunnelInPackets_Object=MibTableColumn
rsIpsecTunnelInPackets=_RsIpsecTunnelInPackets_Object((1,3,6,1,4,1,4355,6,5,1,2,1,30),_RsIpsecTunnelInPackets_Type())
rsIpsecTunnelInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelInPackets.setStatus(_A)
_RsIpsecTunnelOutPackets_Type=Counter32
_RsIpsecTunnelOutPackets_Object=MibTableColumn
rsIpsecTunnelOutPackets=_RsIpsecTunnelOutPackets_Object((1,3,6,1,4,1,4355,6,5,1,2,1,31),_RsIpsecTunnelOutPackets_Type())
rsIpsecTunnelOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelOutPackets.setStatus(_A)
_RsIpsecTunnelInDecryptErrors_Type=Counter32
_RsIpsecTunnelInDecryptErrors_Object=MibTableColumn
rsIpsecTunnelInDecryptErrors=_RsIpsecTunnelInDecryptErrors_Object((1,3,6,1,4,1,4355,6,5,1,2,1,32),_RsIpsecTunnelInDecryptErrors_Type())
rsIpsecTunnelInDecryptErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelInDecryptErrors.setStatus(_A)
_RsIpsecTunnelInAuthErrors_Type=Counter32
_RsIpsecTunnelInAuthErrors_Object=MibTableColumn
rsIpsecTunnelInAuthErrors=_RsIpsecTunnelInAuthErrors_Object((1,3,6,1,4,1,4355,6,5,1,2,1,33),_RsIpsecTunnelInAuthErrors_Type())
rsIpsecTunnelInAuthErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelInAuthErrors.setStatus(_A)
_RsIpsecTunnelInReplayErrors_Type=Counter32
_RsIpsecTunnelInReplayErrors_Object=MibTableColumn
rsIpsecTunnelInReplayErrors=_RsIpsecTunnelInReplayErrors_Object((1,3,6,1,4,1,4355,6,5,1,2,1,34),_RsIpsecTunnelInReplayErrors_Type())
rsIpsecTunnelInReplayErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelInReplayErrors.setStatus(_A)
_RsIpsecTunnelInOtherErrors_Type=Counter32
_RsIpsecTunnelInOtherErrors_Object=MibTableColumn
rsIpsecTunnelInOtherErrors=_RsIpsecTunnelInOtherErrors_Object((1,3,6,1,4,1,4355,6,5,1,2,1,35),_RsIpsecTunnelInOtherErrors_Type())
rsIpsecTunnelInOtherErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelInOtherErrors.setStatus(_A)
_RsIpsecTunnelOutDecryptErrors_Type=Counter32
_RsIpsecTunnelOutDecryptErrors_Object=MibTableColumn
rsIpsecTunnelOutDecryptErrors=_RsIpsecTunnelOutDecryptErrors_Object((1,3,6,1,4,1,4355,6,5,1,2,1,36),_RsIpsecTunnelOutDecryptErrors_Type())
rsIpsecTunnelOutDecryptErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelOutDecryptErrors.setStatus(_A)
_RsIpsecTunnelOutAuthErrors_Type=Counter32
_RsIpsecTunnelOutAuthErrors_Object=MibTableColumn
rsIpsecTunnelOutAuthErrors=_RsIpsecTunnelOutAuthErrors_Object((1,3,6,1,4,1,4355,6,5,1,2,1,37),_RsIpsecTunnelOutAuthErrors_Type())
rsIpsecTunnelOutAuthErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelOutAuthErrors.setStatus(_A)
_RsIpsecTunnelOutReplayErrors_Type=Counter32
_RsIpsecTunnelOutReplayErrors_Object=MibTableColumn
rsIpsecTunnelOutReplayErrors=_RsIpsecTunnelOutReplayErrors_Object((1,3,6,1,4,1,4355,6,5,1,2,1,38),_RsIpsecTunnelOutReplayErrors_Type())
rsIpsecTunnelOutReplayErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelOutReplayErrors.setStatus(_A)
_RsIpsecTunnelOutOtherErrors_Type=Counter32
_RsIpsecTunnelOutOtherErrors_Object=MibTableColumn
rsIpsecTunnelOutOtherErrors=_RsIpsecTunnelOutOtherErrors_Object((1,3,6,1,4,1,4355,6,5,1,2,1,39),_RsIpsecTunnelOutOtherErrors_Type())
rsIpsecTunnelOutOtherErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelOutOtherErrors.setStatus(_A)
class _RsIpsecTunnelUdpEncap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_RsIpsecTunnelUdpEncap_Type.__name__=_C
_RsIpsecTunnelUdpEncap_Object=MibTableColumn
rsIpsecTunnelUdpEncap=_RsIpsecTunnelUdpEncap_Object((1,3,6,1,4,1,4355,6,5,1,2,1,40),_RsIpsecTunnelUdpEncap_Type())
rsIpsecTunnelUdpEncap.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelUdpEncap.setStatus(_A)
class _RsIpsecTunnelPeerUdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RsIpsecTunnelPeerUdpPort_Type.__name__=_C
_RsIpsecTunnelPeerUdpPort_Object=MibTableColumn
rsIpsecTunnelPeerUdpPort=_RsIpsecTunnelPeerUdpPort_Object((1,3,6,1,4,1,4355,6,5,1,2,1,41),_RsIpsecTunnelPeerUdpPort_Type())
rsIpsecTunnelPeerUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelPeerUdpPort.setStatus(_A)
_RsIpsecTunnelOrigPeerAddr_Type=IpAddress
_RsIpsecTunnelOrigPeerAddr_Object=MibTableColumn
rsIpsecTunnelOrigPeerAddr=_RsIpsecTunnelOrigPeerAddr_Object((1,3,6,1,4,1,4355,6,5,1,2,1,42),_RsIpsecTunnelOrigPeerAddr_Type())
rsIpsecTunnelOrigPeerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rsIpsecTunnelOrigPeerAddr.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'rsInfoModule':rsInfoModule,'rsIpsecTunnelMIB':rsIpsecTunnelMIB,'rsIpsecTunnel':rsIpsecTunnel,'rsIpsecTunnelNum':rsIpsecTunnelNum,'rsIpsecTunnelTable':rsIpsecTunnelTable,'rsIpsecTunnelEntry':rsIpsecTunnelEntry,_F:rsIpsecTunnelID,'rsIpsecTunnelLocalAddr':rsIpsecTunnelLocalAddr,'rsIpsecTunnelPeerAddr':rsIpsecTunnelPeerAddr,'rsIpsecTunnelInSpi':rsIpsecTunnelInSpi,'rsIpsecTunnelOutSpi':rsIpsecTunnelOutSpi,'rsIpsecTunnelCreateTime':rsIpsecTunnelCreateTime,'rsIpsecTunnelDeviceID':rsIpsecTunnelDeviceID,'rsIpsecTunnelEspEncryptAlg':rsIpsecTunnelEspEncryptAlg,'rsIpsecTunnelEspAuthAlg':rsIpsecTunnelEspAuthAlg,'rsIpsecTunnelAhAuthAlg':rsIpsecTunnelAhAuthAlg,'rsIpsecTunnelMode':rsIpsecTunnelMode,'rsIpsecTunnelKeyMode':rsIpsecTunnelKeyMode,'rsIpsecTunnelLifeTime':rsIpsecTunnelLifeTime,'rsIpsecTunnelLifeLength':rsIpsecTunnelLifeLength,'rsIpsecTunnelInSaBytes':rsIpsecTunnelInSaBytes,'rsIpsecTunnelOutSaBytes':rsIpsecTunnelOutSaBytes,'rsIpsecTunnelAccSecs':rsIpsecTunnelAccSecs,'rsIpsecTunnelSelectorProtocol':rsIpsecTunnelSelectorProtocol,'rsIpsecTunnelSelectorRemoteIPType':rsIpsecTunnelSelectorRemoteIPType,'rsIpsecTunnelSelectorRemoteIPOne':rsIpsecTunnelSelectorRemoteIPOne,'rsIpsecTunnelSelectorRemoteIPTwo':rsIpsecTunnelSelectorRemoteIPTwo,'rsIpsecTunnelSelectorRemotePort':rsIpsecTunnelSelectorRemotePort,'rsIpsecTunnelSelectorLocalIPType':rsIpsecTunnelSelectorLocalIPType,'rsIpsecTunnelSelectorLocalIPOne':rsIpsecTunnelSelectorLocalIPOne,'rsIpsecTunnelSelectorLocalIPTwo':rsIpsecTunnelSelectorLocalIPTwo,'rsIpsecTunnelSelectorLocalPort':rsIpsecTunnelSelectorLocalPort,'rsIpsecTunnelNumRekey':rsIpsecTunnelNumRekey,'rsIpsecTunnelInKbytes':rsIpsecTunnelInKbytes,'rsIpsecTunnelOutKbytes':rsIpsecTunnelOutKbytes,'rsIpsecTunnelInPackets':rsIpsecTunnelInPackets,'rsIpsecTunnelOutPackets':rsIpsecTunnelOutPackets,'rsIpsecTunnelInDecryptErrors':rsIpsecTunnelInDecryptErrors,'rsIpsecTunnelInAuthErrors':rsIpsecTunnelInAuthErrors,'rsIpsecTunnelInReplayErrors':rsIpsecTunnelInReplayErrors,'rsIpsecTunnelInOtherErrors':rsIpsecTunnelInOtherErrors,'rsIpsecTunnelOutDecryptErrors':rsIpsecTunnelOutDecryptErrors,'rsIpsecTunnelOutAuthErrors':rsIpsecTunnelOutAuthErrors,'rsIpsecTunnelOutReplayErrors':rsIpsecTunnelOutReplayErrors,'rsIpsecTunnelOutOtherErrors':rsIpsecTunnelOutOtherErrors,'rsIpsecTunnelUdpEncap':rsIpsecTunnelUdpEncap,'rsIpsecTunnelPeerUdpPort':rsIpsecTunnelPeerUdpPort,'rsIpsecTunnelOrigPeerAddr':rsIpsecTunnelOrigPeerAddr})