_E='read-write'
_D='eltPortCopyRemoteDirection'
_C='ELTEX-MES-SMON-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols('BRIDGE-MIB','dot1dBasePort')
eltMes,=mibBuilder.importSymbols('ELTEX-MES','eltMes')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
eltMesSmon=ModuleIdentity((1,3,6,1,4,1,35265,1,23,84))
if mibBuilder.loadTexts:eltMesSmon.setRevisions(('2016-02-10 00:00',))
class EltPortCopyRemoteDirectionType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eltPortCopyRemoteRx',1),('eltPortCopyRemoteTx',2)))
_EltPortCopyRemoteTable_Object=MibTable
eltPortCopyRemoteTable=_EltPortCopyRemoteTable_Object((1,3,6,1,4,1,35265,1,23,84,1))
if mibBuilder.loadTexts:eltPortCopyRemoteTable.setStatus(_A)
_EltPortCopyRemoteEntry_Object=MibTableRow
eltPortCopyRemoteEntry=_EltPortCopyRemoteEntry_Object((1,3,6,1,4,1,35265,1,23,84,1,1))
eltPortCopyRemoteEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:eltPortCopyRemoteEntry.setStatus(_A)
_EltPortCopyRemoteDirection_Type=EltPortCopyRemoteDirectionType
_EltPortCopyRemoteDirection_Object=MibTableColumn
eltPortCopyRemoteDirection=_EltPortCopyRemoteDirection_Object((1,3,6,1,4,1,35265,1,23,84,1,1,1),_EltPortCopyRemoteDirection_Type())
eltPortCopyRemoteDirection.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:eltPortCopyRemoteDirection.setStatus(_A)
_EltPortCopyRemoteVlan_Type=VlanId
_EltPortCopyRemoteVlan_Object=MibTableColumn
eltPortCopyRemoteVlan=_EltPortCopyRemoteVlan_Object((1,3,6,1,4,1,35265,1,23,84,1,1,2),_EltPortCopyRemoteVlan_Type())
eltPortCopyRemoteVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:eltPortCopyRemoteVlan.setStatus(_A)
class _EltPortCopyRemotePrio_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_EltPortCopyRemotePrio_Type.__name__=_B
_EltPortCopyRemotePrio_Object=MibTableColumn
eltPortCopyRemotePrio=_EltPortCopyRemotePrio_Object((1,3,6,1,4,1,35265,1,23,84,1,1,3),_EltPortCopyRemotePrio_Type())
eltPortCopyRemotePrio.setMaxAccess(_E)
if mibBuilder.loadTexts:eltPortCopyRemotePrio.setStatus(_A)
_EltPortCopyRemoteStatus_Type=RowStatus
_EltPortCopyRemoteStatus_Object=MibTableColumn
eltPortCopyRemoteStatus=_EltPortCopyRemoteStatus_Object((1,3,6,1,4,1,35265,1,23,84,1,1,4),_EltPortCopyRemoteStatus_Type())
eltPortCopyRemoteStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:eltPortCopyRemoteStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'EltPortCopyRemoteDirectionType':EltPortCopyRemoteDirectionType,'eltMesSmon':eltMesSmon,'eltPortCopyRemoteTable':eltPortCopyRemoteTable,'eltPortCopyRemoteEntry':eltPortCopyRemoteEntry,_D:eltPortCopyRemoteDirection,'eltPortCopyRemoteVlan':eltPortCopyRemoteVlan,'eltPortCopyRemotePrio':eltPortCopyRemotePrio,'eltPortCopyRemoteStatus':eltPortCopyRemoteStatus})