_G='mpeDevSelfTestResults'
_F='PDN-MPE-HEALTH-AND-STATUS-MIB'
_E='DisplayString'
_D='NotificationType'
_C='entPhysicalIndex'
_B='ENTITY-MIB'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_B,_C)
mpe_devHealth,=mibBuilder.importSymbols('PDN-HEADER-MIB','mpe-devHealth')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_D,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_D,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
_MpeDevHealthAndStatusMIBObjects_ObjectIdentity=ObjectIdentity
mpeDevHealthAndStatusMIBObjects=_MpeDevHealthAndStatusMIBObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,7,1))
_MpeDevHealthAndStatusTable_Object=MibTable
mpeDevHealthAndStatusTable=_MpeDevHealthAndStatusTable_Object((1,3,6,1,4,1,1795,2,24,12,7,1,1))
if mibBuilder.loadTexts:mpeDevHealthAndStatusTable.setStatus(_A)
_MpeDevHealthAndStatusEntry_Object=MibTableRow
mpeDevHealthAndStatusEntry=_MpeDevHealthAndStatusEntry_Object((1,3,6,1,4,1,1795,2,24,12,7,1,1,1))
mpeDevHealthAndStatusEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:mpeDevHealthAndStatusEntry.setStatus(_A)
class _MpeDevSelfTestResults_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MpeDevSelfTestResults_Type.__name__=_E
_MpeDevSelfTestResults_Object=MibTableColumn
mpeDevSelfTestResults=_MpeDevSelfTestResults_Object((1,3,6,1,4,1,1795,2,24,12,7,1,1,1,1),_MpeDevSelfTestResults_Type())
mpeDevSelfTestResults.setMaxAccess('read-only')
if mibBuilder.loadTexts:mpeDevSelfTestResults.setStatus(_A)
_MpeDevHealthAndStatusMIBTraps_ObjectIdentity=ObjectIdentity
mpeDevHealthAndStatusMIBTraps=_MpeDevHealthAndStatusMIBTraps_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,7,2))
mpeSelfTestFailure=NotificationType((1,3,6,1,4,1,1795,2,24,12,7,2,0,1))
mpeSelfTestFailure.setObjects((_F,_G))
if mibBuilder.loadTexts:mpeSelfTestFailure.setStatus('')
mibBuilder.exportSymbols(_F,**{'mpeDevHealthAndStatusMIBObjects':mpeDevHealthAndStatusMIBObjects,'mpeDevHealthAndStatusTable':mpeDevHealthAndStatusTable,'mpeDevHealthAndStatusEntry':mpeDevHealthAndStatusEntry,_G:mpeDevSelfTestResults,'mpeDevHealthAndStatusMIBTraps':mpeDevHealthAndStatusMIBTraps,'mpeSelfTestFailure':mpeSelfTestFailure})