_F='fsLdpTcpConnectionId'
_E='SUPERMICRO-LDP-TEST-MIB'
_D='DisplayString'
_C='Unsigned32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention')
fsLdpTestMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,1,13,14))
if mibBuilder.loadTexts:fsLdpTestMIB.setRevisions(('2012-11-30 00:00',))
_FsLdpTestObjects_ObjectIdentity=ObjectIdentity
fsLdpTestObjects=_FsLdpTestObjects_ObjectIdentity((1,3,6,1,4,1,10876,101,1,13,14,1))
_FsLdpTcpConnectionTable_Object=MibTable
fsLdpTcpConnectionTable=_FsLdpTcpConnectionTable_Object((1,3,6,1,4,1,10876,101,1,13,14,1,1))
if mibBuilder.loadTexts:fsLdpTcpConnectionTable.setStatus(_A)
_FsLdpTcpConnectionEntry_Object=MibTableRow
fsLdpTcpConnectionEntry=_FsLdpTcpConnectionEntry_Object((1,3,6,1,4,1,10876,101,1,13,14,1,1,1))
fsLdpTcpConnectionEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:fsLdpTcpConnectionEntry.setStatus(_A)
class _FsLdpTcpConnectionId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_FsLdpTcpConnectionId_Type.__name__=_C
_FsLdpTcpConnectionId_Object=MibTableColumn
fsLdpTcpConnectionId=_FsLdpTcpConnectionId_Object((1,3,6,1,4,1,10876,101,1,13,14,1,1,1,1),_FsLdpTcpConnectionId_Type())
fsLdpTcpConnectionId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fsLdpTcpConnectionId.setStatus(_A)
_FsLdpTcpDestIpAddress_Type=IpAddress
_FsLdpTcpDestIpAddress_Object=MibTableColumn
fsLdpTcpDestIpAddress=_FsLdpTcpDestIpAddress_Object((1,3,6,1,4,1,10876,101,1,13,14,1,1,1,2),_FsLdpTcpDestIpAddress_Type())
fsLdpTcpDestIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLdpTcpDestIpAddress.setStatus(_A)
_FsLdpTcpSourceIpAddress_Type=IpAddress
_FsLdpTcpSourceIpAddress_Object=MibTableColumn
fsLdpTcpSourceIpAddress=_FsLdpTcpSourceIpAddress_Object((1,3,6,1,4,1,10876,101,1,13,14,1,1,1,3),_FsLdpTcpSourceIpAddress_Type())
fsLdpTcpSourceIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLdpTcpSourceIpAddress.setStatus(_A)
class _FsLdpTcpDestPort_Type(Unsigned32):defaultValue=646;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsLdpTcpDestPort_Type.__name__=_C
_FsLdpTcpDestPort_Object=MibTableColumn
fsLdpTcpDestPort=_FsLdpTcpDestPort_Object((1,3,6,1,4,1,10876,101,1,13,14,1,1,1,4),_FsLdpTcpDestPort_Type())
fsLdpTcpDestPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLdpTcpDestPort.setStatus(_A)
class _FsLdpTcpSourcePort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsLdpTcpSourcePort_Type.__name__=_C
_FsLdpTcpSourcePort_Object=MibTableColumn
fsLdpTcpSourcePort=_FsLdpTcpSourcePort_Object((1,3,6,1,4,1,10876,101,1,13,14,1,1,1,5),_FsLdpTcpSourcePort_Type())
fsLdpTcpSourcePort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLdpTcpSourcePort.setStatus(_A)
class _FsLdpTcpPacketTxValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1500))
_FsLdpTcpPacketTxValue_Type.__name__=_D
_FsLdpTcpPacketTxValue_Object=MibTableColumn
fsLdpTcpPacketTxValue=_FsLdpTcpPacketTxValue_Object((1,3,6,1,4,1,10876,101,1,13,14,1,1,1,6),_FsLdpTcpPacketTxValue_Type())
fsLdpTcpPacketTxValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLdpTcpPacketTxValue.setStatus(_A)
_FsLdpTcpConnectionRowStatus_Type=RowStatus
_FsLdpTcpConnectionRowStatus_Object=MibTableColumn
fsLdpTcpConnectionRowStatus=_FsLdpTcpConnectionRowStatus_Object((1,3,6,1,4,1,10876,101,1,13,14,1,1,1,7),_FsLdpTcpConnectionRowStatus_Type())
fsLdpTcpConnectionRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLdpTcpConnectionRowStatus.setStatus(_A)
class _FsLdpTcpVrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsLdpTcpVrfName_Type.__name__=_D
_FsLdpTcpVrfName_Object=MibTableColumn
fsLdpTcpVrfName=_FsLdpTcpVrfName_Object((1,3,6,1,4,1,10876,101,1,13,14,1,1,1,8),_FsLdpTcpVrfName_Type())
fsLdpTcpVrfName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLdpTcpVrfName.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'fsLdpTestMIB':fsLdpTestMIB,'fsLdpTestObjects':fsLdpTestObjects,'fsLdpTcpConnectionTable':fsLdpTcpConnectionTable,'fsLdpTcpConnectionEntry':fsLdpTcpConnectionEntry,_F:fsLdpTcpConnectionId,'fsLdpTcpDestIpAddress':fsLdpTcpDestIpAddress,'fsLdpTcpSourceIpAddress':fsLdpTcpSourceIpAddress,'fsLdpTcpDestPort':fsLdpTcpDestPort,'fsLdpTcpSourcePort':fsLdpTcpSourcePort,'fsLdpTcpPacketTxValue':fsLdpTcpPacketTxValue,'fsLdpTcpConnectionRowStatus':fsLdpTcpConnectionRowStatus,'fsLdpTcpVrfName':fsLdpTcpVrfName})