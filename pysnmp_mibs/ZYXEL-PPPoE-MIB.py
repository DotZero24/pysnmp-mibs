_K='zyPppoeIaPortVlanVid'
_J='read-create'
_I='not-accessible'
_H='zyPppoeIaVlanVid'
_G='read-only'
_F='ZYXEL-PPPoE-MIB'
_E='dot1dBasePort'
_D='BRIDGE-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_D,_E)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelPppoe=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,67))
_ZyxelPppoeIaSetup_ObjectIdentity=ObjectIdentity
zyxelPppoeIaSetup=_ZyxelPppoeIaSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,67,1))
_ZyPppoeIaState_Type=EnabledStatus
_ZyPppoeIaState_Object=MibScalar
zyPppoeIaState=_ZyPppoeIaState_Object((1,3,6,1,4,1,890,1,15,3,67,1,1),_ZyPppoeIaState_Type())
zyPppoeIaState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPppoeIaState.setStatus(_A)
_ZyPppoeIaAccessNodeIdString_Type=DisplayString
_ZyPppoeIaAccessNodeIdString_Object=MibScalar
zyPppoeIaAccessNodeIdString=_ZyPppoeIaAccessNodeIdString_Object((1,3,6,1,4,1,890,1,15,3,67,1,2),_ZyPppoeIaAccessNodeIdString_Type())
zyPppoeIaAccessNodeIdString.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPppoeIaAccessNodeIdString.setStatus(_A)
_ZyPppoeIaFlexibleCircuitIdSyntaxState_Type=EnabledStatus
_ZyPppoeIaFlexibleCircuitIdSyntaxState_Object=MibScalar
zyPppoeIaFlexibleCircuitIdSyntaxState=_ZyPppoeIaFlexibleCircuitIdSyntaxState_Object((1,3,6,1,4,1,890,1,15,3,67,1,3),_ZyPppoeIaFlexibleCircuitIdSyntaxState_Type())
zyPppoeIaFlexibleCircuitIdSyntaxState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPppoeIaFlexibleCircuitIdSyntaxState.setStatus(_A)
_ZyPppoeIaFlexibleCircuitIdSyntaxIdString_Type=DisplayString
_ZyPppoeIaFlexibleCircuitIdSyntaxIdString_Object=MibScalar
zyPppoeIaFlexibleCircuitIdSyntaxIdString=_ZyPppoeIaFlexibleCircuitIdSyntaxIdString_Object((1,3,6,1,4,1,890,1,15,3,67,1,4),_ZyPppoeIaFlexibleCircuitIdSyntaxIdString_Type())
zyPppoeIaFlexibleCircuitIdSyntaxIdString.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPppoeIaFlexibleCircuitIdSyntaxIdString.setStatus(_A)
class _ZyPppoeIaFlexibleCircuitIdSyntaxOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('sp',1),('sv',2),('pv',3),('spv',4)))
_ZyPppoeIaFlexibleCircuitIdSyntaxOption_Type.__name__=_C
_ZyPppoeIaFlexibleCircuitIdSyntaxOption_Object=MibScalar
zyPppoeIaFlexibleCircuitIdSyntaxOption=_ZyPppoeIaFlexibleCircuitIdSyntaxOption_Object((1,3,6,1,4,1,890,1,15,3,67,1,5),_ZyPppoeIaFlexibleCircuitIdSyntaxOption_Type())
zyPppoeIaFlexibleCircuitIdSyntaxOption.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPppoeIaFlexibleCircuitIdSyntaxOption.setStatus(_A)
class _ZyPppoeIaFlexibleCircuitIdSyntaxDelimiter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('poundSign',1),('dot',2),('comma',3),('semicolon',4),('slash',5),('space',6)))
_ZyPppoeIaFlexibleCircuitIdSyntaxDelimiter_Type.__name__=_C
_ZyPppoeIaFlexibleCircuitIdSyntaxDelimiter_Object=MibScalar
zyPppoeIaFlexibleCircuitIdSyntaxDelimiter=_ZyPppoeIaFlexibleCircuitIdSyntaxDelimiter_Object((1,3,6,1,4,1,890,1,15,3,67,1,6),_ZyPppoeIaFlexibleCircuitIdSyntaxDelimiter_Type())
zyPppoeIaFlexibleCircuitIdSyntaxDelimiter.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPppoeIaFlexibleCircuitIdSyntaxDelimiter.setStatus(_A)
_ZyxelPppoeIaPortTable_Object=MibTable
zyxelPppoeIaPortTable=_ZyxelPppoeIaPortTable_Object((1,3,6,1,4,1,890,1,15,3,67,1,7))
if mibBuilder.loadTexts:zyxelPppoeIaPortTable.setStatus(_A)
_ZyxelPppoeIaPortEntry_Object=MibTableRow
zyxelPppoeIaPortEntry=_ZyxelPppoeIaPortEntry_Object((1,3,6,1,4,1,890,1,15,3,67,1,7,1))
zyxelPppoeIaPortEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zyxelPppoeIaPortEntry.setStatus(_A)
_ZyPppoeIaPortTrustState_Type=EnabledStatus
_ZyPppoeIaPortTrustState_Object=MibTableColumn
zyPppoeIaPortTrustState=_ZyPppoeIaPortTrustState_Object((1,3,6,1,4,1,890,1,15,3,67,1,7,1,1),_ZyPppoeIaPortTrustState_Type())
zyPppoeIaPortTrustState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPppoeIaPortTrustState.setStatus(_A)
_ZyPppoeIaPortCircuitIdString_Type=DisplayString
_ZyPppoeIaPortCircuitIdString_Object=MibTableColumn
zyPppoeIaPortCircuitIdString=_ZyPppoeIaPortCircuitIdString_Object((1,3,6,1,4,1,890,1,15,3,67,1,7,1,2),_ZyPppoeIaPortCircuitIdString_Type())
zyPppoeIaPortCircuitIdString.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPppoeIaPortCircuitIdString.setStatus(_A)
_ZyPppoeIaPortRemoteIdString_Type=DisplayString
_ZyPppoeIaPortRemoteIdString_Object=MibTableColumn
zyPppoeIaPortRemoteIdString=_ZyPppoeIaPortRemoteIdString_Object((1,3,6,1,4,1,890,1,15,3,67,1,7,1,3),_ZyPppoeIaPortRemoteIdString_Type())
zyPppoeIaPortRemoteIdString.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPppoeIaPortRemoteIdString.setStatus(_A)
_ZyPppoeIaMaxNumberOfVlans_Type=Integer32
_ZyPppoeIaMaxNumberOfVlans_Object=MibScalar
zyPppoeIaMaxNumberOfVlans=_ZyPppoeIaMaxNumberOfVlans_Object((1,3,6,1,4,1,890,1,15,3,67,1,8),_ZyPppoeIaMaxNumberOfVlans_Type())
zyPppoeIaMaxNumberOfVlans.setMaxAccess(_G)
if mibBuilder.loadTexts:zyPppoeIaMaxNumberOfVlans.setStatus(_A)
_ZyxelPppoeIaVlanTable_Object=MibTable
zyxelPppoeIaVlanTable=_ZyxelPppoeIaVlanTable_Object((1,3,6,1,4,1,890,1,15,3,67,1,9))
if mibBuilder.loadTexts:zyxelPppoeIaVlanTable.setStatus(_A)
_ZyxelPppoeIaVlanEntry_Object=MibTableRow
zyxelPppoeIaVlanEntry=_ZyxelPppoeIaVlanEntry_Object((1,3,6,1,4,1,890,1,15,3,67,1,9,1))
zyxelPppoeIaVlanEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:zyxelPppoeIaVlanEntry.setStatus(_A)
class _ZyPppoeIaVlanVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZyPppoeIaVlanVid_Type.__name__=_C
_ZyPppoeIaVlanVid_Object=MibTableColumn
zyPppoeIaVlanVid=_ZyPppoeIaVlanVid_Object((1,3,6,1,4,1,890,1,15,3,67,1,9,1,1),_ZyPppoeIaVlanVid_Type())
zyPppoeIaVlanVid.setMaxAccess(_I)
if mibBuilder.loadTexts:zyPppoeIaVlanVid.setStatus(_A)
_ZyPppoeIaVlanCircuitIdState_Type=EnabledStatus
_ZyPppoeIaVlanCircuitIdState_Object=MibTableColumn
zyPppoeIaVlanCircuitIdState=_ZyPppoeIaVlanCircuitIdState_Object((1,3,6,1,4,1,890,1,15,3,67,1,9,1,2),_ZyPppoeIaVlanCircuitIdState_Type())
zyPppoeIaVlanCircuitIdState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPppoeIaVlanCircuitIdState.setStatus(_A)
_ZyPppoeIaVlanRemoteIdState_Type=EnabledStatus
_ZyPppoeIaVlanRemoteIdState_Object=MibTableColumn
zyPppoeIaVlanRemoteIdState=_ZyPppoeIaVlanRemoteIdState_Object((1,3,6,1,4,1,890,1,15,3,67,1,9,1,3),_ZyPppoeIaVlanRemoteIdState_Type())
zyPppoeIaVlanRemoteIdState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPppoeIaVlanRemoteIdState.setStatus(_A)
_ZyPppoeIaVlanRowStatus_Type=RowStatus
_ZyPppoeIaVlanRowStatus_Object=MibTableColumn
zyPppoeIaVlanRowStatus=_ZyPppoeIaVlanRowStatus_Object((1,3,6,1,4,1,890,1,15,3,67,1,9,1,4),_ZyPppoeIaVlanRowStatus_Type())
zyPppoeIaVlanRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:zyPppoeIaVlanRowStatus.setStatus(_A)
_ZyPppoeIaMaxNumberOfPortVlans_Type=Integer32
_ZyPppoeIaMaxNumberOfPortVlans_Object=MibScalar
zyPppoeIaMaxNumberOfPortVlans=_ZyPppoeIaMaxNumberOfPortVlans_Object((1,3,6,1,4,1,890,1,15,3,67,1,10),_ZyPppoeIaMaxNumberOfPortVlans_Type())
zyPppoeIaMaxNumberOfPortVlans.setMaxAccess(_G)
if mibBuilder.loadTexts:zyPppoeIaMaxNumberOfPortVlans.setStatus(_A)
_ZyxelPppoeIaPortVlanTable_Object=MibTable
zyxelPppoeIaPortVlanTable=_ZyxelPppoeIaPortVlanTable_Object((1,3,6,1,4,1,890,1,15,3,67,1,11))
if mibBuilder.loadTexts:zyxelPppoeIaPortVlanTable.setStatus(_A)
_ZyxelPppoeIaPortVlanEntry_Object=MibTableRow
zyxelPppoeIaPortVlanEntry=_ZyxelPppoeIaPortVlanEntry_Object((1,3,6,1,4,1,890,1,15,3,67,1,11,1))
zyxelPppoeIaPortVlanEntry.setIndexNames((0,_D,_E),(0,_F,_K))
if mibBuilder.loadTexts:zyxelPppoeIaPortVlanEntry.setStatus(_A)
_ZyPppoeIaPortVlanVid_Type=Integer32
_ZyPppoeIaPortVlanVid_Object=MibTableColumn
zyPppoeIaPortVlanVid=_ZyPppoeIaPortVlanVid_Object((1,3,6,1,4,1,890,1,15,3,67,1,11,1,1),_ZyPppoeIaPortVlanVid_Type())
zyPppoeIaPortVlanVid.setMaxAccess(_I)
if mibBuilder.loadTexts:zyPppoeIaPortVlanVid.setStatus(_A)
_ZyPppoeIaPortVlanCircuitIdString_Type=DisplayString
_ZyPppoeIaPortVlanCircuitIdString_Object=MibTableColumn
zyPppoeIaPortVlanCircuitIdString=_ZyPppoeIaPortVlanCircuitIdString_Object((1,3,6,1,4,1,890,1,15,3,67,1,11,1,2),_ZyPppoeIaPortVlanCircuitIdString_Type())
zyPppoeIaPortVlanCircuitIdString.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPppoeIaPortVlanCircuitIdString.setStatus(_A)
_ZyPppoeIaPortVlanRemoteIdString_Type=DisplayString
_ZyPppoeIaPortVlanRemoteIdString_Object=MibTableColumn
zyPppoeIaPortVlanRemoteIdString=_ZyPppoeIaPortVlanRemoteIdString_Object((1,3,6,1,4,1,890,1,15,3,67,1,11,1,3),_ZyPppoeIaPortVlanRemoteIdString_Type())
zyPppoeIaPortVlanRemoteIdString.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPppoeIaPortVlanRemoteIdString.setStatus(_A)
_ZyPppoeIaPortVlanRowStatus_Type=RowStatus
_ZyPppoeIaPortVlanRowStatus_Object=MibTableColumn
zyPppoeIaPortVlanRowStatus=_ZyPppoeIaPortVlanRowStatus_Object((1,3,6,1,4,1,890,1,15,3,67,1,11,1,4),_ZyPppoeIaPortVlanRowStatus_Type())
zyPppoeIaPortVlanRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:zyPppoeIaPortVlanRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'zyxelPppoe':zyxelPppoe,'zyxelPppoeIaSetup':zyxelPppoeIaSetup,'zyPppoeIaState':zyPppoeIaState,'zyPppoeIaAccessNodeIdString':zyPppoeIaAccessNodeIdString,'zyPppoeIaFlexibleCircuitIdSyntaxState':zyPppoeIaFlexibleCircuitIdSyntaxState,'zyPppoeIaFlexibleCircuitIdSyntaxIdString':zyPppoeIaFlexibleCircuitIdSyntaxIdString,'zyPppoeIaFlexibleCircuitIdSyntaxOption':zyPppoeIaFlexibleCircuitIdSyntaxOption,'zyPppoeIaFlexibleCircuitIdSyntaxDelimiter':zyPppoeIaFlexibleCircuitIdSyntaxDelimiter,'zyxelPppoeIaPortTable':zyxelPppoeIaPortTable,'zyxelPppoeIaPortEntry':zyxelPppoeIaPortEntry,'zyPppoeIaPortTrustState':zyPppoeIaPortTrustState,'zyPppoeIaPortCircuitIdString':zyPppoeIaPortCircuitIdString,'zyPppoeIaPortRemoteIdString':zyPppoeIaPortRemoteIdString,'zyPppoeIaMaxNumberOfVlans':zyPppoeIaMaxNumberOfVlans,'zyxelPppoeIaVlanTable':zyxelPppoeIaVlanTable,'zyxelPppoeIaVlanEntry':zyxelPppoeIaVlanEntry,_H:zyPppoeIaVlanVid,'zyPppoeIaVlanCircuitIdState':zyPppoeIaVlanCircuitIdState,'zyPppoeIaVlanRemoteIdState':zyPppoeIaVlanRemoteIdState,'zyPppoeIaVlanRowStatus':zyPppoeIaVlanRowStatus,'zyPppoeIaMaxNumberOfPortVlans':zyPppoeIaMaxNumberOfPortVlans,'zyxelPppoeIaPortVlanTable':zyxelPppoeIaPortVlanTable,'zyxelPppoeIaPortVlanEntry':zyxelPppoeIaPortVlanEntry,_K:zyPppoeIaPortVlanVid,'zyPppoeIaPortVlanCircuitIdString':zyPppoeIaPortVlanCircuitIdString,'zyPppoeIaPortVlanRemoteIdString':zyPppoeIaPortVlanRemoteIdString,'zyPppoeIaPortVlanRowStatus':zyPppoeIaPortVlanRowStatus})