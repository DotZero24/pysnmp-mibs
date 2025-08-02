_J='Kbytes'
_I='ip-addr-range'
_H='ip-addr-subnet'
_G='ip-addr-single'
_F='wgIpsecTunnelID'
_E='WATCHGUARD-IPSEC-TUNNEL-MIB'
_D='unknown'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
watchguard,=mibBuilder.importSymbols('WATCHGUARD-SMI','watchguard')
wgInfoModule=ModuleIdentity((1,3,6,1,4,1,3097,6))
if mibBuilder.loadTexts:wgInfoModule.setRevisions(('2007-01-25 12:00',))
_WgIpsecTunnelMIB_ObjectIdentity=ObjectIdentity
wgIpsecTunnelMIB=_WgIpsecTunnelMIB_ObjectIdentity((1,3,6,1,4,1,3097,6,5))
if mibBuilder.loadTexts:wgIpsecTunnelMIB.setStatus(_A)
_WgIpsecTunnel_ObjectIdentity=ObjectIdentity
wgIpsecTunnel=_WgIpsecTunnel_ObjectIdentity((1,3,6,1,4,1,3097,6,5,1))
if mibBuilder.loadTexts:wgIpsecTunnel.setStatus(_A)
_WgIpsecTunnelNum_Type=Unsigned32
_WgIpsecTunnelNum_Object=MibScalar
wgIpsecTunnelNum=_WgIpsecTunnelNum_Object((1,3,6,1,4,1,3097,6,5,1,1),_WgIpsecTunnelNum_Type())
wgIpsecTunnelNum.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelNum.setStatus(_A)
_WgIpsecTunnelTable_Object=MibTable
wgIpsecTunnelTable=_WgIpsecTunnelTable_Object((1,3,6,1,4,1,3097,6,5,1,2))
if mibBuilder.loadTexts:wgIpsecTunnelTable.setStatus(_A)
_WgIpsecTunnelEntry_Object=MibTableRow
wgIpsecTunnelEntry=_WgIpsecTunnelEntry_Object((1,3,6,1,4,1,3097,6,5,1,2,1))
wgIpsecTunnelEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:wgIpsecTunnelEntry.setStatus(_A)
_WgIpsecTunnelID_Type=Integer32
_WgIpsecTunnelID_Object=MibTableColumn
wgIpsecTunnelID=_WgIpsecTunnelID_Object((1,3,6,1,4,1,3097,6,5,1,2,1,1),_WgIpsecTunnelID_Type())
wgIpsecTunnelID.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelID.setStatus(_A)
_WgIpsecTunnelLocalAddr_Type=IpAddress
_WgIpsecTunnelLocalAddr_Object=MibTableColumn
wgIpsecTunnelLocalAddr=_WgIpsecTunnelLocalAddr_Object((1,3,6,1,4,1,3097,6,5,1,2,1,2),_WgIpsecTunnelLocalAddr_Type())
wgIpsecTunnelLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelLocalAddr.setStatus(_A)
_WgIpsecTunnelPeerAddr_Type=IpAddress
_WgIpsecTunnelPeerAddr_Object=MibTableColumn
wgIpsecTunnelPeerAddr=_WgIpsecTunnelPeerAddr_Object((1,3,6,1,4,1,3097,6,5,1,2,1,3),_WgIpsecTunnelPeerAddr_Type())
wgIpsecTunnelPeerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelPeerAddr.setStatus(_A)
_WgIpsecTunnelInSpi_Type=Unsigned32
_WgIpsecTunnelInSpi_Object=MibTableColumn
wgIpsecTunnelInSpi=_WgIpsecTunnelInSpi_Object((1,3,6,1,4,1,3097,6,5,1,2,1,4),_WgIpsecTunnelInSpi_Type())
wgIpsecTunnelInSpi.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelInSpi.setStatus(_A)
_WgIpsecTunnelOutSpi_Type=Unsigned32
_WgIpsecTunnelOutSpi_Object=MibTableColumn
wgIpsecTunnelOutSpi=_WgIpsecTunnelOutSpi_Object((1,3,6,1,4,1,3097,6,5,1,2,1,5),_WgIpsecTunnelOutSpi_Type())
wgIpsecTunnelOutSpi.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelOutSpi.setStatus(_A)
_WgIpsecTunnelCreateTime_Type=DateAndTime
_WgIpsecTunnelCreateTime_Object=MibTableColumn
wgIpsecTunnelCreateTime=_WgIpsecTunnelCreateTime_Object((1,3,6,1,4,1,3097,6,5,1,2,1,6),_WgIpsecTunnelCreateTime_Type())
wgIpsecTunnelCreateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelCreateTime.setStatus(_A)
_WgIpsecTunnelDeviceID_Type=Unsigned32
_WgIpsecTunnelDeviceID_Object=MibTableColumn
wgIpsecTunnelDeviceID=_WgIpsecTunnelDeviceID_Object((1,3,6,1,4,1,3097,6,5,1,2,1,7),_WgIpsecTunnelDeviceID_Type())
wgIpsecTunnelDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelDeviceID.setStatus(_A)
class _WgIpsecTunnelEspEncryptAlg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4)));namedValues=NamedValues(*((_D,0),('des',2),('three-des',3),('aes',4)))
_WgIpsecTunnelEspEncryptAlg_Type.__name__=_C
_WgIpsecTunnelEspEncryptAlg_Object=MibTableColumn
wgIpsecTunnelEspEncryptAlg=_WgIpsecTunnelEspEncryptAlg_Object((1,3,6,1,4,1,3097,6,5,1,2,1,8),_WgIpsecTunnelEspEncryptAlg_Type())
wgIpsecTunnelEspEncryptAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelEspEncryptAlg.setStatus(_A)
class _WgIpsecTunnelEspAuthAlg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3)));namedValues=NamedValues(*((_D,0),('md5',2),('sha',3)))
_WgIpsecTunnelEspAuthAlg_Type.__name__=_C
_WgIpsecTunnelEspAuthAlg_Object=MibTableColumn
wgIpsecTunnelEspAuthAlg=_WgIpsecTunnelEspAuthAlg_Object((1,3,6,1,4,1,3097,6,5,1,2,1,9),_WgIpsecTunnelEspAuthAlg_Type())
wgIpsecTunnelEspAuthAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelEspAuthAlg.setStatus(_A)
class _WgIpsecTunnelAhAuthAlg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3)));namedValues=NamedValues(*((_D,0),('md5',2),('sha',3)))
_WgIpsecTunnelAhAuthAlg_Type.__name__=_C
_WgIpsecTunnelAhAuthAlg_Object=MibTableColumn
wgIpsecTunnelAhAuthAlg=_WgIpsecTunnelAhAuthAlg_Object((1,3,6,1,4,1,3097,6,5,1,2,1,10),_WgIpsecTunnelAhAuthAlg_Type())
wgIpsecTunnelAhAuthAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelAhAuthAlg.setStatus(_A)
class _WgIpsecTunnelMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),('tunnel',1),('transport',2)))
_WgIpsecTunnelMode_Type.__name__=_C
_WgIpsecTunnelMode_Object=MibTableColumn
wgIpsecTunnelMode=_WgIpsecTunnelMode_Object((1,3,6,1,4,1,3097,6,5,1,2,1,11),_WgIpsecTunnelMode_Type())
wgIpsecTunnelMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelMode.setStatus(_A)
class _WgIpsecTunnelKeyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),('manual',1),('auto-ike',2),('other',3)))
_WgIpsecTunnelKeyMode_Type.__name__=_C
_WgIpsecTunnelKeyMode_Object=MibTableColumn
wgIpsecTunnelKeyMode=_WgIpsecTunnelKeyMode_Object((1,3,6,1,4,1,3097,6,5,1,2,1,12),_WgIpsecTunnelKeyMode_Type())
wgIpsecTunnelKeyMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelKeyMode.setStatus(_A)
_WgIpsecTunnelLifeTime_Type=TimeTicks
_WgIpsecTunnelLifeTime_Object=MibTableColumn
wgIpsecTunnelLifeTime=_WgIpsecTunnelLifeTime_Object((1,3,6,1,4,1,3097,6,5,1,2,1,13),_WgIpsecTunnelLifeTime_Type())
wgIpsecTunnelLifeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelLifeTime.setStatus(_A)
_WgIpsecTunnelLifeLength_Type=Counter64
_WgIpsecTunnelLifeLength_Object=MibTableColumn
wgIpsecTunnelLifeLength=_WgIpsecTunnelLifeLength_Object((1,3,6,1,4,1,3097,6,5,1,2,1,14),_WgIpsecTunnelLifeLength_Type())
wgIpsecTunnelLifeLength.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelLifeLength.setStatus(_A)
_WgIpsecTunnelInSaBytes_Type=Counter64
_WgIpsecTunnelInSaBytes_Object=MibTableColumn
wgIpsecTunnelInSaBytes=_WgIpsecTunnelInSaBytes_Object((1,3,6,1,4,1,3097,6,5,1,2,1,15),_WgIpsecTunnelInSaBytes_Type())
wgIpsecTunnelInSaBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelInSaBytes.setStatus(_A)
_WgIpsecTunnelOutSaBytes_Type=Counter64
_WgIpsecTunnelOutSaBytes_Object=MibTableColumn
wgIpsecTunnelOutSaBytes=_WgIpsecTunnelOutSaBytes_Object((1,3,6,1,4,1,3097,6,5,1,2,1,16),_WgIpsecTunnelOutSaBytes_Type())
wgIpsecTunnelOutSaBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelOutSaBytes.setStatus(_A)
_WgIpsecTunnelAccSecs_Type=Counter32
_WgIpsecTunnelAccSecs_Object=MibTableColumn
wgIpsecTunnelAccSecs=_WgIpsecTunnelAccSecs_Object((1,3,6,1,4,1,3097,6,5,1,2,1,17),_WgIpsecTunnelAccSecs_Type())
wgIpsecTunnelAccSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelAccSecs.setStatus(_A)
class _WgIpsecTunnelSelectorProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,6,8,12,17,22,29,41,43,44,46,47,50,51,58,59,60,92,98,103,255)));namedValues=NamedValues(*(('any',0),('icmp',1),('igmp',2),('ipip',4),('tcp',6),('egp',8),('pup',12),('udp',17),('idp',22),('tp',29),('ipv6',41),('ipv6-routing',43),('ipv6-fragmentation',44),('rsvp',46),('gre',47),('esp',50),('ah',51),('icmpv6',58),('none',59),('dstopts',60),('mtp',92),('encap',98),('pim',103),('raw',255)))
_WgIpsecTunnelSelectorProtocol_Type.__name__=_C
_WgIpsecTunnelSelectorProtocol_Object=MibTableColumn
wgIpsecTunnelSelectorProtocol=_WgIpsecTunnelSelectorProtocol_Object((1,3,6,1,4,1,3097,6,5,1,2,1,18),_WgIpsecTunnelSelectorProtocol_Type())
wgIpsecTunnelSelectorProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelSelectorProtocol.setStatus(_A)
class _WgIpsecTunnelSelectorRemoteIPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_WgIpsecTunnelSelectorRemoteIPType_Type.__name__=_C
_WgIpsecTunnelSelectorRemoteIPType_Object=MibTableColumn
wgIpsecTunnelSelectorRemoteIPType=_WgIpsecTunnelSelectorRemoteIPType_Object((1,3,6,1,4,1,3097,6,5,1,2,1,19),_WgIpsecTunnelSelectorRemoteIPType_Type())
wgIpsecTunnelSelectorRemoteIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelSelectorRemoteIPType.setStatus(_A)
_WgIpsecTunnelSelectorRemoteIPOne_Type=IpAddress
_WgIpsecTunnelSelectorRemoteIPOne_Object=MibTableColumn
wgIpsecTunnelSelectorRemoteIPOne=_WgIpsecTunnelSelectorRemoteIPOne_Object((1,3,6,1,4,1,3097,6,5,1,2,1,20),_WgIpsecTunnelSelectorRemoteIPOne_Type())
wgIpsecTunnelSelectorRemoteIPOne.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelSelectorRemoteIPOne.setStatus(_A)
_WgIpsecTunnelSelectorRemoteIPTwo_Type=IpAddress
_WgIpsecTunnelSelectorRemoteIPTwo_Object=MibTableColumn
wgIpsecTunnelSelectorRemoteIPTwo=_WgIpsecTunnelSelectorRemoteIPTwo_Object((1,3,6,1,4,1,3097,6,5,1,2,1,21),_WgIpsecTunnelSelectorRemoteIPTwo_Type())
wgIpsecTunnelSelectorRemoteIPTwo.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelSelectorRemoteIPTwo.setStatus(_A)
class _WgIpsecTunnelSelectorRemotePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WgIpsecTunnelSelectorRemotePort_Type.__name__=_C
_WgIpsecTunnelSelectorRemotePort_Object=MibTableColumn
wgIpsecTunnelSelectorRemotePort=_WgIpsecTunnelSelectorRemotePort_Object((1,3,6,1,4,1,3097,6,5,1,2,1,22),_WgIpsecTunnelSelectorRemotePort_Type())
wgIpsecTunnelSelectorRemotePort.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelSelectorRemotePort.setStatus(_A)
class _WgIpsecTunnelSelectorLocalIPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_WgIpsecTunnelSelectorLocalIPType_Type.__name__=_C
_WgIpsecTunnelSelectorLocalIPType_Object=MibTableColumn
wgIpsecTunnelSelectorLocalIPType=_WgIpsecTunnelSelectorLocalIPType_Object((1,3,6,1,4,1,3097,6,5,1,2,1,23),_WgIpsecTunnelSelectorLocalIPType_Type())
wgIpsecTunnelSelectorLocalIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelSelectorLocalIPType.setStatus(_A)
_WgIpsecTunnelSelectorLocalIPOne_Type=IpAddress
_WgIpsecTunnelSelectorLocalIPOne_Object=MibTableColumn
wgIpsecTunnelSelectorLocalIPOne=_WgIpsecTunnelSelectorLocalIPOne_Object((1,3,6,1,4,1,3097,6,5,1,2,1,24),_WgIpsecTunnelSelectorLocalIPOne_Type())
wgIpsecTunnelSelectorLocalIPOne.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelSelectorLocalIPOne.setStatus(_A)
_WgIpsecTunnelSelectorLocalIPTwo_Type=IpAddress
_WgIpsecTunnelSelectorLocalIPTwo_Object=MibTableColumn
wgIpsecTunnelSelectorLocalIPTwo=_WgIpsecTunnelSelectorLocalIPTwo_Object((1,3,6,1,4,1,3097,6,5,1,2,1,25),_WgIpsecTunnelSelectorLocalIPTwo_Type())
wgIpsecTunnelSelectorLocalIPTwo.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelSelectorLocalIPTwo.setStatus(_A)
class _WgIpsecTunnelSelectorLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WgIpsecTunnelSelectorLocalPort_Type.__name__=_C
_WgIpsecTunnelSelectorLocalPort_Object=MibTableColumn
wgIpsecTunnelSelectorLocalPort=_WgIpsecTunnelSelectorLocalPort_Object((1,3,6,1,4,1,3097,6,5,1,2,1,26),_WgIpsecTunnelSelectorLocalPort_Type())
wgIpsecTunnelSelectorLocalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelSelectorLocalPort.setStatus(_A)
_WgIpsecTunnelNumRekey_Type=Counter32
_WgIpsecTunnelNumRekey_Object=MibTableColumn
wgIpsecTunnelNumRekey=_WgIpsecTunnelNumRekey_Object((1,3,6,1,4,1,3097,6,5,1,2,1,27),_WgIpsecTunnelNumRekey_Type())
wgIpsecTunnelNumRekey.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelNumRekey.setStatus(_A)
_WgIpsecTunnelInKbytes_Type=Counter64
_WgIpsecTunnelInKbytes_Object=MibTableColumn
wgIpsecTunnelInKbytes=_WgIpsecTunnelInKbytes_Object((1,3,6,1,4,1,3097,6,5,1,2,1,28),_WgIpsecTunnelInKbytes_Type())
wgIpsecTunnelInKbytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelInKbytes.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecTunnelInKbytes.setUnits(_J)
_WgIpsecTunnelOutKbytes_Type=Counter64
_WgIpsecTunnelOutKbytes_Object=MibTableColumn
wgIpsecTunnelOutKbytes=_WgIpsecTunnelOutKbytes_Object((1,3,6,1,4,1,3097,6,5,1,2,1,29),_WgIpsecTunnelOutKbytes_Type())
wgIpsecTunnelOutKbytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelOutKbytes.setStatus(_A)
if mibBuilder.loadTexts:wgIpsecTunnelOutKbytes.setUnits(_J)
_WgIpsecTunnelInPackets_Type=Counter64
_WgIpsecTunnelInPackets_Object=MibTableColumn
wgIpsecTunnelInPackets=_WgIpsecTunnelInPackets_Object((1,3,6,1,4,1,3097,6,5,1,2,1,30),_WgIpsecTunnelInPackets_Type())
wgIpsecTunnelInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelInPackets.setStatus(_A)
_WgIpsecTunnelOutPackets_Type=Counter64
_WgIpsecTunnelOutPackets_Object=MibTableColumn
wgIpsecTunnelOutPackets=_WgIpsecTunnelOutPackets_Object((1,3,6,1,4,1,3097,6,5,1,2,1,31),_WgIpsecTunnelOutPackets_Type())
wgIpsecTunnelOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelOutPackets.setStatus(_A)
_WgIpsecTunnelInDecryptErrors_Type=Counter32
_WgIpsecTunnelInDecryptErrors_Object=MibTableColumn
wgIpsecTunnelInDecryptErrors=_WgIpsecTunnelInDecryptErrors_Object((1,3,6,1,4,1,3097,6,5,1,2,1,32),_WgIpsecTunnelInDecryptErrors_Type())
wgIpsecTunnelInDecryptErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelInDecryptErrors.setStatus(_A)
_WgIpsecTunnelInAuthErrors_Type=Counter32
_WgIpsecTunnelInAuthErrors_Object=MibTableColumn
wgIpsecTunnelInAuthErrors=_WgIpsecTunnelInAuthErrors_Object((1,3,6,1,4,1,3097,6,5,1,2,1,33),_WgIpsecTunnelInAuthErrors_Type())
wgIpsecTunnelInAuthErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelInAuthErrors.setStatus(_A)
_WgIpsecTunnelInReplayErrors_Type=Counter32
_WgIpsecTunnelInReplayErrors_Object=MibTableColumn
wgIpsecTunnelInReplayErrors=_WgIpsecTunnelInReplayErrors_Object((1,3,6,1,4,1,3097,6,5,1,2,1,34),_WgIpsecTunnelInReplayErrors_Type())
wgIpsecTunnelInReplayErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelInReplayErrors.setStatus(_A)
_WgIpsecTunnelInOtherErrors_Type=Counter32
_WgIpsecTunnelInOtherErrors_Object=MibTableColumn
wgIpsecTunnelInOtherErrors=_WgIpsecTunnelInOtherErrors_Object((1,3,6,1,4,1,3097,6,5,1,2,1,35),_WgIpsecTunnelInOtherErrors_Type())
wgIpsecTunnelInOtherErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelInOtherErrors.setStatus(_A)
_WgIpsecTunnelOutDecryptErrors_Type=Counter32
_WgIpsecTunnelOutDecryptErrors_Object=MibTableColumn
wgIpsecTunnelOutDecryptErrors=_WgIpsecTunnelOutDecryptErrors_Object((1,3,6,1,4,1,3097,6,5,1,2,1,36),_WgIpsecTunnelOutDecryptErrors_Type())
wgIpsecTunnelOutDecryptErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelOutDecryptErrors.setStatus(_A)
_WgIpsecTunnelOutAuthErrors_Type=Counter32
_WgIpsecTunnelOutAuthErrors_Object=MibTableColumn
wgIpsecTunnelOutAuthErrors=_WgIpsecTunnelOutAuthErrors_Object((1,3,6,1,4,1,3097,6,5,1,2,1,37),_WgIpsecTunnelOutAuthErrors_Type())
wgIpsecTunnelOutAuthErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelOutAuthErrors.setStatus(_A)
_WgIpsecTunnelOutReplayErrors_Type=Counter32
_WgIpsecTunnelOutReplayErrors_Object=MibTableColumn
wgIpsecTunnelOutReplayErrors=_WgIpsecTunnelOutReplayErrors_Object((1,3,6,1,4,1,3097,6,5,1,2,1,38),_WgIpsecTunnelOutReplayErrors_Type())
wgIpsecTunnelOutReplayErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelOutReplayErrors.setStatus(_A)
_WgIpsecTunnelOutOtherErrors_Type=Counter32
_WgIpsecTunnelOutOtherErrors_Object=MibTableColumn
wgIpsecTunnelOutOtherErrors=_WgIpsecTunnelOutOtherErrors_Object((1,3,6,1,4,1,3097,6,5,1,2,1,39),_WgIpsecTunnelOutOtherErrors_Type())
wgIpsecTunnelOutOtherErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelOutOtherErrors.setStatus(_A)
class _WgIpsecTunnelUdpEncap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_WgIpsecTunnelUdpEncap_Type.__name__=_C
_WgIpsecTunnelUdpEncap_Object=MibTableColumn
wgIpsecTunnelUdpEncap=_WgIpsecTunnelUdpEncap_Object((1,3,6,1,4,1,3097,6,5,1,2,1,40),_WgIpsecTunnelUdpEncap_Type())
wgIpsecTunnelUdpEncap.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelUdpEncap.setStatus(_A)
class _WgIpsecTunnelPeerUdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WgIpsecTunnelPeerUdpPort_Type.__name__=_C
_WgIpsecTunnelPeerUdpPort_Object=MibTableColumn
wgIpsecTunnelPeerUdpPort=_WgIpsecTunnelPeerUdpPort_Object((1,3,6,1,4,1,3097,6,5,1,2,1,41),_WgIpsecTunnelPeerUdpPort_Type())
wgIpsecTunnelPeerUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelPeerUdpPort.setStatus(_A)
_WgIpsecTunnelOrigPeerAddr_Type=IpAddress
_WgIpsecTunnelOrigPeerAddr_Object=MibTableColumn
wgIpsecTunnelOrigPeerAddr=_WgIpsecTunnelOrigPeerAddr_Object((1,3,6,1,4,1,3097,6,5,1,2,1,42),_WgIpsecTunnelOrigPeerAddr_Type())
wgIpsecTunnelOrigPeerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wgIpsecTunnelOrigPeerAddr.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'wgInfoModule':wgInfoModule,'wgIpsecTunnelMIB':wgIpsecTunnelMIB,'wgIpsecTunnel':wgIpsecTunnel,'wgIpsecTunnelNum':wgIpsecTunnelNum,'wgIpsecTunnelTable':wgIpsecTunnelTable,'wgIpsecTunnelEntry':wgIpsecTunnelEntry,_F:wgIpsecTunnelID,'wgIpsecTunnelLocalAddr':wgIpsecTunnelLocalAddr,'wgIpsecTunnelPeerAddr':wgIpsecTunnelPeerAddr,'wgIpsecTunnelInSpi':wgIpsecTunnelInSpi,'wgIpsecTunnelOutSpi':wgIpsecTunnelOutSpi,'wgIpsecTunnelCreateTime':wgIpsecTunnelCreateTime,'wgIpsecTunnelDeviceID':wgIpsecTunnelDeviceID,'wgIpsecTunnelEspEncryptAlg':wgIpsecTunnelEspEncryptAlg,'wgIpsecTunnelEspAuthAlg':wgIpsecTunnelEspAuthAlg,'wgIpsecTunnelAhAuthAlg':wgIpsecTunnelAhAuthAlg,'wgIpsecTunnelMode':wgIpsecTunnelMode,'wgIpsecTunnelKeyMode':wgIpsecTunnelKeyMode,'wgIpsecTunnelLifeTime':wgIpsecTunnelLifeTime,'wgIpsecTunnelLifeLength':wgIpsecTunnelLifeLength,'wgIpsecTunnelInSaBytes':wgIpsecTunnelInSaBytes,'wgIpsecTunnelOutSaBytes':wgIpsecTunnelOutSaBytes,'wgIpsecTunnelAccSecs':wgIpsecTunnelAccSecs,'wgIpsecTunnelSelectorProtocol':wgIpsecTunnelSelectorProtocol,'wgIpsecTunnelSelectorRemoteIPType':wgIpsecTunnelSelectorRemoteIPType,'wgIpsecTunnelSelectorRemoteIPOne':wgIpsecTunnelSelectorRemoteIPOne,'wgIpsecTunnelSelectorRemoteIPTwo':wgIpsecTunnelSelectorRemoteIPTwo,'wgIpsecTunnelSelectorRemotePort':wgIpsecTunnelSelectorRemotePort,'wgIpsecTunnelSelectorLocalIPType':wgIpsecTunnelSelectorLocalIPType,'wgIpsecTunnelSelectorLocalIPOne':wgIpsecTunnelSelectorLocalIPOne,'wgIpsecTunnelSelectorLocalIPTwo':wgIpsecTunnelSelectorLocalIPTwo,'wgIpsecTunnelSelectorLocalPort':wgIpsecTunnelSelectorLocalPort,'wgIpsecTunnelNumRekey':wgIpsecTunnelNumRekey,'wgIpsecTunnelInKbytes':wgIpsecTunnelInKbytes,'wgIpsecTunnelOutKbytes':wgIpsecTunnelOutKbytes,'wgIpsecTunnelInPackets':wgIpsecTunnelInPackets,'wgIpsecTunnelOutPackets':wgIpsecTunnelOutPackets,'wgIpsecTunnelInDecryptErrors':wgIpsecTunnelInDecryptErrors,'wgIpsecTunnelInAuthErrors':wgIpsecTunnelInAuthErrors,'wgIpsecTunnelInReplayErrors':wgIpsecTunnelInReplayErrors,'wgIpsecTunnelInOtherErrors':wgIpsecTunnelInOtherErrors,'wgIpsecTunnelOutDecryptErrors':wgIpsecTunnelOutDecryptErrors,'wgIpsecTunnelOutAuthErrors':wgIpsecTunnelOutAuthErrors,'wgIpsecTunnelOutReplayErrors':wgIpsecTunnelOutReplayErrors,'wgIpsecTunnelOutOtherErrors':wgIpsecTunnelOutOtherErrors,'wgIpsecTunnelUdpEncap':wgIpsecTunnelUdpEncap,'wgIpsecTunnelPeerUdpPort':wgIpsecTunnelPeerUdpPort,'wgIpsecTunnelOrigPeerAddr':wgIpsecTunnelOrigPeerAddr})