_H='ifIndex'
_G='IF-MIB'
_F='Unsigned32'
_E='dot1xPaePortNumber'
_D='IEEE8021-PAE-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGen802dot1x,adGen802dot1xID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGen802dot1x','adGen802dot1xID')
dot1xPaePortNumber,=mibBuilder.importSymbols(_D,_E)
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_G,'InterfaceIndex',_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGen802dot1xMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,17,1))
if mibBuilder.loadTexts:adGen802dot1xMIB.setRevisions(('2013-06-27 00:00','2013-06-19 00:00'))
_AdGen802dot1xEapolConfigTable_Object=MibTable
adGen802dot1xEapolConfigTable=_AdGen802dot1xEapolConfigTable_Object((1,3,6,1,4,1,664,5,70,17,1))
if mibBuilder.loadTexts:adGen802dot1xEapolConfigTable.setStatus(_A)
_AdGen802dot1xEapolConfigEntry_Object=MibTableRow
adGen802dot1xEapolConfigEntry=_AdGen802dot1xEapolConfigEntry_Object((1,3,6,1,4,1,664,5,70,17,1,1))
adGen802dot1xEapolConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:adGen802dot1xEapolConfigEntry.setStatus(_A)
class _AdGen802dot1xEapRespTimeout_Type(Unsigned32):defaultValue=30
_AdGen802dot1xEapRespTimeout_Type.__name__=_F
_AdGen802dot1xEapRespTimeout_Object=MibTableColumn
adGen802dot1xEapRespTimeout=_AdGen802dot1xEapRespTimeout_Object((1,3,6,1,4,1,664,5,70,17,1,1,1),_AdGen802dot1xEapRespTimeout_Type())
adGen802dot1xEapRespTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:adGen802dot1xEapRespTimeout.setStatus(_A)
class _AdGen802dot1xMaxEapReq_Type(Unsigned32):defaultValue=2
_AdGen802dot1xMaxEapReq_Type.__name__=_F
_AdGen802dot1xMaxEapReq_Object=MibTableColumn
adGen802dot1xMaxEapReq=_AdGen802dot1xMaxEapReq_Object((1,3,6,1,4,1,664,5,70,17,1,1,2),_AdGen802dot1xMaxEapReq_Type())
adGen802dot1xMaxEapReq.setMaxAccess(_B)
if mibBuilder.loadTexts:adGen802dot1xMaxEapReq.setStatus(_A)
_AdGen802dot1xPortConfigTable_Object=MibTable
adGen802dot1xPortConfigTable=_AdGen802dot1xPortConfigTable_Object((1,3,6,1,4,1,664,5,70,17,2))
if mibBuilder.loadTexts:adGen802dot1xPortConfigTable.setStatus(_A)
_AdGen802dot1xPortConfigEntry_Object=MibTableRow
adGen802dot1xPortConfigEntry=_AdGen802dot1xPortConfigEntry_Object((1,3,6,1,4,1,664,5,70,17,2,1))
adGen802dot1xPortConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:adGen802dot1xPortConfigEntry.setStatus(_A)
class _AdGen802dot1xPortIPEntity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('ipHost',2),('subtendedHost',3)))
_AdGen802dot1xPortIPEntity_Type.__name__=_C
_AdGen802dot1xPortIPEntity_Object=MibTableColumn
adGen802dot1xPortIPEntity=_AdGen802dot1xPortIPEntity_Object((1,3,6,1,4,1,664,5,70,17,2,1,1),_AdGen802dot1xPortIPEntity_Type())
adGen802dot1xPortIPEntity.setMaxAccess(_B)
if mibBuilder.loadTexts:adGen802dot1xPortIPEntity.setStatus(_A)
_AdGen802dot1xPortIPHostName_Type=DisplayString
_AdGen802dot1xPortIPHostName_Object=MibTableColumn
adGen802dot1xPortIPHostName=_AdGen802dot1xPortIPHostName_Object((1,3,6,1,4,1,664,5,70,17,2,1,2),_AdGen802dot1xPortIPHostName_Type())
adGen802dot1xPortIPHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:adGen802dot1xPortIPHostName.setStatus(_A)
class _AdGen802dot1xPortAuthServerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('radius',1))
_AdGen802dot1xPortAuthServerType_Type.__name__=_C
_AdGen802dot1xPortAuthServerType_Object=MibTableColumn
adGen802dot1xPortAuthServerType=_AdGen802dot1xPortAuthServerType_Object((1,3,6,1,4,1,664,5,70,17,2,1,3),_AdGen802dot1xPortAuthServerType_Type())
adGen802dot1xPortAuthServerType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGen802dot1xPortAuthServerType.setStatus(_A)
_AdGen802dot1xPortRadiusServerGroupName_Type=DisplayString
_AdGen802dot1xPortRadiusServerGroupName_Object=MibTableColumn
adGen802dot1xPortRadiusServerGroupName=_AdGen802dot1xPortRadiusServerGroupName_Object((1,3,6,1,4,1,664,5,70,17,2,1,4),_AdGen802dot1xPortRadiusServerGroupName_Type())
adGen802dot1xPortRadiusServerGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:adGen802dot1xPortRadiusServerGroupName.setStatus(_A)
_AdGen802dot1xPortStatusTable_Object=MibTable
adGen802dot1xPortStatusTable=_AdGen802dot1xPortStatusTable_Object((1,3,6,1,4,1,664,5,70,17,3))
if mibBuilder.loadTexts:adGen802dot1xPortStatusTable.setStatus(_A)
_AdGen802dot1xPortStatusEntry_Object=MibTableRow
adGen802dot1xPortStatusEntry=_AdGen802dot1xPortStatusEntry_Object((1,3,6,1,4,1,664,5,70,17,3,1))
adGen802dot1xPortStatusEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:adGen802dot1xPortStatusEntry.setStatus(_A)
_AdGen802dot1xPortStatusLastError_Type=DisplayString
_AdGen802dot1xPortStatusLastError_Object=MibTableColumn
adGen802dot1xPortStatusLastError=_AdGen802dot1xPortStatusLastError_Object((1,3,6,1,4,1,664,5,70,17,3,1,1),_AdGen802dot1xPortStatusLastError_Type())
adGen802dot1xPortStatusLastError.setMaxAccess('read-only')
if mibBuilder.loadTexts:adGen802dot1xPortStatusLastError.setStatus(_A)
class _AdGen802dot1xPortStatusClearCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clear',1))
_AdGen802dot1xPortStatusClearCounters_Type.__name__=_C
_AdGen802dot1xPortStatusClearCounters_Object=MibTableColumn
adGen802dot1xPortStatusClearCounters=_AdGen802dot1xPortStatusClearCounters_Object((1,3,6,1,4,1,664,5,70,17,3,1,2),_AdGen802dot1xPortStatusClearCounters_Type())
adGen802dot1xPortStatusClearCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:adGen802dot1xPortStatusClearCounters.setStatus(_A)
mibBuilder.exportSymbols('ADTRAN-IEEE8021X-MIB',**{'adGen802dot1xEapolConfigTable':adGen802dot1xEapolConfigTable,'adGen802dot1xEapolConfigEntry':adGen802dot1xEapolConfigEntry,'adGen802dot1xEapRespTimeout':adGen802dot1xEapRespTimeout,'adGen802dot1xMaxEapReq':adGen802dot1xMaxEapReq,'adGen802dot1xPortConfigTable':adGen802dot1xPortConfigTable,'adGen802dot1xPortConfigEntry':adGen802dot1xPortConfigEntry,'adGen802dot1xPortIPEntity':adGen802dot1xPortIPEntity,'adGen802dot1xPortIPHostName':adGen802dot1xPortIPHostName,'adGen802dot1xPortAuthServerType':adGen802dot1xPortAuthServerType,'adGen802dot1xPortRadiusServerGroupName':adGen802dot1xPortRadiusServerGroupName,'adGen802dot1xPortStatusTable':adGen802dot1xPortStatusTable,'adGen802dot1xPortStatusEntry':adGen802dot1xPortStatusEntry,'adGen802dot1xPortStatusLastError':adGen802dot1xPortStatusLastError,'adGen802dot1xPortStatusClearCounters':adGen802dot1xPortStatusClearCounters,'adGen802dot1xMIB':adGen802dot1xMIB})