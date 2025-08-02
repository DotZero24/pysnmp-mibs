_E='zyRouteDomainIpMaskBits'
_D='zyRouteDomainIpAddress'
_C='read-write'
_B='ZYXEL-IP-FORWARD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyRouteDomainIpAddress,zyRouteDomainIpMaskBits=mibBuilder.importSymbols(_B,_D,_E)
zyxelDvmrp=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,23))
_ZyxelDvmrpSetup_ObjectIdentity=ObjectIdentity
zyxelDvmrpSetup=_ZyxelDvmrpSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,23,1))
_ZyDvmrpState_Type=EnabledStatus
_ZyDvmrpState_Object=MibScalar
zyDvmrpState=_ZyDvmrpState_Object((1,3,6,1,4,1,890,1,15,3,23,1,1),_ZyDvmrpState_Type())
zyDvmrpState.setMaxAccess(_C)
if mibBuilder.loadTexts:zyDvmrpState.setStatus(_A)
_ZyDvmrpThreshold_Type=Integer32
_ZyDvmrpThreshold_Object=MibScalar
zyDvmrpThreshold=_ZyDvmrpThreshold_Object((1,3,6,1,4,1,890,1,15,3,23,1,2),_ZyDvmrpThreshold_Type())
zyDvmrpThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:zyDvmrpThreshold.setStatus(_A)
_ZyxelDvmrpRouteDomainTable_Object=MibTable
zyxelDvmrpRouteDomainTable=_ZyxelDvmrpRouteDomainTable_Object((1,3,6,1,4,1,890,1,15,3,23,1,3))
if mibBuilder.loadTexts:zyxelDvmrpRouteDomainTable.setStatus(_A)
_ZyxelDvmrpRouteDomainEntry_Object=MibTableRow
zyxelDvmrpRouteDomainEntry=_ZyxelDvmrpRouteDomainEntry_Object((1,3,6,1,4,1,890,1,15,3,23,1,3,1))
zyxelDvmrpRouteDomainEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:zyxelDvmrpRouteDomainEntry.setStatus(_A)
_ZyDvmrpRouteDomainState_Type=EnabledStatus
_ZyDvmrpRouteDomainState_Object=MibTableColumn
zyDvmrpRouteDomainState=_ZyDvmrpRouteDomainState_Object((1,3,6,1,4,1,890,1,15,3,23,1,3,1,1),_ZyDvmrpRouteDomainState_Type())
zyDvmrpRouteDomainState.setMaxAccess(_C)
if mibBuilder.loadTexts:zyDvmrpRouteDomainState.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-DVMRP-MIB',**{'zyxelDvmrp':zyxelDvmrp,'zyxelDvmrpSetup':zyxelDvmrpSetup,'zyDvmrpState':zyDvmrpState,'zyDvmrpThreshold':zyDvmrpThreshold,'zyxelDvmrpRouteDomainTable':zyxelDvmrpRouteDomainTable,'zyxelDvmrpRouteDomainEntry':zyxelDvmrpRouteDomainEntry,'zyDvmrpRouteDomainState':zyDvmrpRouteDomainState})