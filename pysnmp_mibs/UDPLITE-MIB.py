_a='udpliteAppGroup'
_Z='udpliteEndpointGroup'
_Y='udplitePartialCsumGroup'
_X='udpliteBaseGroup'
_W='udpliteEndpointViolCoverage'
_V='udpliteEndpointMinCoverage'
_U='udpliteEndpointProcess'
_T='udpliteOutPartialCov'
_S='udpliteInBadChecksum'
_R='udpliteInPartialCov'
_Q='udpliteStatsDiscontinuityTime'
_P='udpliteOutDatagrams'
_O='udpliteInErrors'
_N='udpliteNoPorts'
_M='udpliteInDatagrams'
_L='udpliteEndpointInstance'
_K='udpliteEndpointRemotePort'
_J='udpliteEndpointRemoteAddress'
_I='udpliteEndpointRemoteAddressType'
_H='udpliteEndpointLocalPort'
_G='udpliteEndpointLocalAddress'
_F='udpliteEndpointLocalAddressType'
_E='Unsigned32'
_D='not-accessible'
_C='read-only'
_B='UDPLITE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
udpliteMIB=ModuleIdentity((1,3,6,1,2,1,170))
if mibBuilder.loadTexts:udpliteMIB.setRevisions(('2007-12-18 00:00',))
_Udplite_ObjectIdentity=ObjectIdentity
udplite=_Udplite_ObjectIdentity((1,3,6,1,2,1,170,1))
_UdpliteInDatagrams_Type=Counter64
_UdpliteInDatagrams_Object=MibScalar
udpliteInDatagrams=_UdpliteInDatagrams_Object((1,3,6,1,2,1,170,1,1),_UdpliteInDatagrams_Type())
udpliteInDatagrams.setMaxAccess(_C)
if mibBuilder.loadTexts:udpliteInDatagrams.setStatus(_A)
_UdpliteInPartialCov_Type=Counter64
_UdpliteInPartialCov_Object=MibScalar
udpliteInPartialCov=_UdpliteInPartialCov_Object((1,3,6,1,2,1,170,1,2),_UdpliteInPartialCov_Type())
udpliteInPartialCov.setMaxAccess(_C)
if mibBuilder.loadTexts:udpliteInPartialCov.setStatus(_A)
_UdpliteNoPorts_Type=Counter32
_UdpliteNoPorts_Object=MibScalar
udpliteNoPorts=_UdpliteNoPorts_Object((1,3,6,1,2,1,170,1,3),_UdpliteNoPorts_Type())
udpliteNoPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:udpliteNoPorts.setStatus(_A)
_UdpliteInErrors_Type=Counter32
_UdpliteInErrors_Object=MibScalar
udpliteInErrors=_UdpliteInErrors_Object((1,3,6,1,2,1,170,1,4),_UdpliteInErrors_Type())
udpliteInErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:udpliteInErrors.setStatus(_A)
_UdpliteInBadChecksum_Type=Counter32
_UdpliteInBadChecksum_Object=MibScalar
udpliteInBadChecksum=_UdpliteInBadChecksum_Object((1,3,6,1,2,1,170,1,5),_UdpliteInBadChecksum_Type())
udpliteInBadChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:udpliteInBadChecksum.setStatus(_A)
_UdpliteOutDatagrams_Type=Counter64
_UdpliteOutDatagrams_Object=MibScalar
udpliteOutDatagrams=_UdpliteOutDatagrams_Object((1,3,6,1,2,1,170,1,6),_UdpliteOutDatagrams_Type())
udpliteOutDatagrams.setMaxAccess(_C)
if mibBuilder.loadTexts:udpliteOutDatagrams.setStatus(_A)
_UdpliteOutPartialCov_Type=Counter64
_UdpliteOutPartialCov_Object=MibScalar
udpliteOutPartialCov=_UdpliteOutPartialCov_Object((1,3,6,1,2,1,170,1,7),_UdpliteOutPartialCov_Type())
udpliteOutPartialCov.setMaxAccess(_C)
if mibBuilder.loadTexts:udpliteOutPartialCov.setStatus(_A)
_UdpliteEndpointTable_Object=MibTable
udpliteEndpointTable=_UdpliteEndpointTable_Object((1,3,6,1,2,1,170,1,8))
if mibBuilder.loadTexts:udpliteEndpointTable.setStatus(_A)
_UdpliteEndpointEntry_Object=MibTableRow
udpliteEndpointEntry=_UdpliteEndpointEntry_Object((1,3,6,1,2,1,170,1,8,1))
udpliteEndpointEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H),(0,_B,_I),(0,_B,_J),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:udpliteEndpointEntry.setStatus(_A)
_UdpliteEndpointLocalAddressType_Type=InetAddressType
_UdpliteEndpointLocalAddressType_Object=MibTableColumn
udpliteEndpointLocalAddressType=_UdpliteEndpointLocalAddressType_Object((1,3,6,1,2,1,170,1,8,1,1),_UdpliteEndpointLocalAddressType_Type())
udpliteEndpointLocalAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:udpliteEndpointLocalAddressType.setStatus(_A)
_UdpliteEndpointLocalAddress_Type=InetAddress
_UdpliteEndpointLocalAddress_Object=MibTableColumn
udpliteEndpointLocalAddress=_UdpliteEndpointLocalAddress_Object((1,3,6,1,2,1,170,1,8,1,2),_UdpliteEndpointLocalAddress_Type())
udpliteEndpointLocalAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:udpliteEndpointLocalAddress.setStatus(_A)
_UdpliteEndpointLocalPort_Type=InetPortNumber
_UdpliteEndpointLocalPort_Object=MibTableColumn
udpliteEndpointLocalPort=_UdpliteEndpointLocalPort_Object((1,3,6,1,2,1,170,1,8,1,3),_UdpliteEndpointLocalPort_Type())
udpliteEndpointLocalPort.setMaxAccess(_D)
if mibBuilder.loadTexts:udpliteEndpointLocalPort.setStatus(_A)
_UdpliteEndpointRemoteAddressType_Type=InetAddressType
_UdpliteEndpointRemoteAddressType_Object=MibTableColumn
udpliteEndpointRemoteAddressType=_UdpliteEndpointRemoteAddressType_Object((1,3,6,1,2,1,170,1,8,1,4),_UdpliteEndpointRemoteAddressType_Type())
udpliteEndpointRemoteAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:udpliteEndpointRemoteAddressType.setStatus(_A)
_UdpliteEndpointRemoteAddress_Type=InetAddress
_UdpliteEndpointRemoteAddress_Object=MibTableColumn
udpliteEndpointRemoteAddress=_UdpliteEndpointRemoteAddress_Object((1,3,6,1,2,1,170,1,8,1,5),_UdpliteEndpointRemoteAddress_Type())
udpliteEndpointRemoteAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:udpliteEndpointRemoteAddress.setStatus(_A)
_UdpliteEndpointRemotePort_Type=InetPortNumber
_UdpliteEndpointRemotePort_Object=MibTableColumn
udpliteEndpointRemotePort=_UdpliteEndpointRemotePort_Object((1,3,6,1,2,1,170,1,8,1,6),_UdpliteEndpointRemotePort_Type())
udpliteEndpointRemotePort.setMaxAccess(_D)
if mibBuilder.loadTexts:udpliteEndpointRemotePort.setStatus(_A)
class _UdpliteEndpointInstance_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_UdpliteEndpointInstance_Type.__name__=_E
_UdpliteEndpointInstance_Object=MibTableColumn
udpliteEndpointInstance=_UdpliteEndpointInstance_Object((1,3,6,1,2,1,170,1,8,1,7),_UdpliteEndpointInstance_Type())
udpliteEndpointInstance.setMaxAccess(_D)
if mibBuilder.loadTexts:udpliteEndpointInstance.setStatus(_A)
_UdpliteEndpointProcess_Type=Unsigned32
_UdpliteEndpointProcess_Object=MibTableColumn
udpliteEndpointProcess=_UdpliteEndpointProcess_Object((1,3,6,1,2,1,170,1,8,1,8),_UdpliteEndpointProcess_Type())
udpliteEndpointProcess.setMaxAccess(_C)
if mibBuilder.loadTexts:udpliteEndpointProcess.setStatus(_A)
_UdpliteEndpointMinCoverage_Type=Unsigned32
_UdpliteEndpointMinCoverage_Object=MibTableColumn
udpliteEndpointMinCoverage=_UdpliteEndpointMinCoverage_Object((1,3,6,1,2,1,170,1,8,1,9),_UdpliteEndpointMinCoverage_Type())
udpliteEndpointMinCoverage.setMaxAccess(_C)
if mibBuilder.loadTexts:udpliteEndpointMinCoverage.setStatus(_A)
_UdpliteEndpointViolCoverage_Type=Counter32
_UdpliteEndpointViolCoverage_Object=MibTableColumn
udpliteEndpointViolCoverage=_UdpliteEndpointViolCoverage_Object((1,3,6,1,2,1,170,1,8,1,10),_UdpliteEndpointViolCoverage_Type())
udpliteEndpointViolCoverage.setMaxAccess(_C)
if mibBuilder.loadTexts:udpliteEndpointViolCoverage.setStatus(_A)
_UdpliteStatsDiscontinuityTime_Type=TimeStamp
_UdpliteStatsDiscontinuityTime_Object=MibScalar
udpliteStatsDiscontinuityTime=_UdpliteStatsDiscontinuityTime_Object((1,3,6,1,2,1,170,1,9),_UdpliteStatsDiscontinuityTime_Type())
udpliteStatsDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:udpliteStatsDiscontinuityTime.setStatus(_A)
_UdpliteMIBConformance_ObjectIdentity=ObjectIdentity
udpliteMIBConformance=_UdpliteMIBConformance_ObjectIdentity((1,3,6,1,2,1,170,2))
_UdpliteMIBGroups_ObjectIdentity=ObjectIdentity
udpliteMIBGroups=_UdpliteMIBGroups_ObjectIdentity((1,3,6,1,2,1,170,2,2))
udpliteBaseGroup=ObjectGroup((1,3,6,1,2,1,170,2,2,1))
udpliteBaseGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:udpliteBaseGroup.setStatus(_A)
udplitePartialCsumGroup=ObjectGroup((1,3,6,1,2,1,170,2,2,2))
udplitePartialCsumGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:udplitePartialCsumGroup.setStatus(_A)
udpliteEndpointGroup=ObjectGroup((1,3,6,1,2,1,170,2,2,3))
udpliteEndpointGroup.setObjects(*((_B,_U),(_B,_V)))
if mibBuilder.loadTexts:udpliteEndpointGroup.setStatus(_A)
udpliteAppGroup=ObjectGroup((1,3,6,1,2,1,170,2,2,4))
udpliteAppGroup.setObjects((_B,_W))
if mibBuilder.loadTexts:udpliteAppGroup.setStatus(_A)
udpliteMIBCompliance=ModuleCompliance((1,3,6,1,2,1,170,2,1))
udpliteMIBCompliance.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:udpliteMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'udpliteMIB':udpliteMIB,'udplite':udplite,_M:udpliteInDatagrams,_R:udpliteInPartialCov,_N:udpliteNoPorts,_O:udpliteInErrors,_S:udpliteInBadChecksum,_P:udpliteOutDatagrams,_T:udpliteOutPartialCov,'udpliteEndpointTable':udpliteEndpointTable,'udpliteEndpointEntry':udpliteEndpointEntry,_F:udpliteEndpointLocalAddressType,_G:udpliteEndpointLocalAddress,_H:udpliteEndpointLocalPort,_I:udpliteEndpointRemoteAddressType,_J:udpliteEndpointRemoteAddress,_K:udpliteEndpointRemotePort,_L:udpliteEndpointInstance,_U:udpliteEndpointProcess,_V:udpliteEndpointMinCoverage,_W:udpliteEndpointViolCoverage,_Q:udpliteStatsDiscontinuityTime,'udpliteMIBConformance':udpliteMIBConformance,'udpliteMIBCompliance':udpliteMIBCompliance,'udpliteMIBGroups':udpliteMIBGroups,_X:udpliteBaseGroup,_Y:udplitePartialCsumGroup,_Z:udpliteEndpointGroup,_a:udpliteAppGroup})