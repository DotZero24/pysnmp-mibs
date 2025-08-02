_H='oaSubscrDirection'
_G='oaSubscrName'
_F='NotificationType'
_E='OASUBSCR-CFG-MIB'
_D='other'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_F,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_F,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class SubscriberName(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,35))
class DirectionType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('ingress',2),('egress',3)))
class AccountCouter(Counter32):0
class AccountCounter64(Counter64):0
_Nbase_ObjectIdentity=ObjectIdentity
nbase=_Nbase_ObjectIdentity((1,3,6,1,4,1,629))
_NbSwitchG1_ObjectIdentity=ObjectIdentity
nbSwitchG1=_NbSwitchG1_ObjectIdentity((1,3,6,1,4,1,629,1))
_NbSwitchG1Il_ObjectIdentity=ObjectIdentity
nbSwitchG1Il=_NbSwitchG1Il_ObjectIdentity((1,3,6,1,4,1,629,1,50))
_OaSubscriberConfig_ObjectIdentity=ObjectIdentity
oaSubscriberConfig=_OaSubscriberConfig_ObjectIdentity((1,3,6,1,4,1,629,1,50,15))
_OaSubscrConfigGen_ObjectIdentity=ObjectIdentity
oaSubscrConfigGen=_OaSubscrConfigGen_ObjectIdentity((1,3,6,1,4,1,629,1,50,15,1))
_OaSubscrAccounting_ObjectIdentity=ObjectIdentity
oaSubscrAccounting=_OaSubscrAccounting_ObjectIdentity((1,3,6,1,4,1,629,1,50,15,6))
_OaSubscrAccNameTable_Object=MibTable
oaSubscrAccNameTable=_OaSubscrAccNameTable_Object((1,3,6,1,4,1,629,1,50,15,6,10))
if mibBuilder.loadTexts:oaSubscrAccNameTable.setStatus(_A)
_OaSubscrAccNameEntry_Object=MibTableRow
oaSubscrAccNameEntry=_OaSubscrAccNameEntry_Object((1,3,6,1,4,1,629,1,50,15,6,10,1))
oaSubscrAccNameEntry.setIndexNames((0,_E,_G),(0,_E,_H))
if mibBuilder.loadTexts:oaSubscrAccNameEntry.setStatus(_A)
_OaSubscrName_Type=SubscriberName
_OaSubscrName_Object=MibTableColumn
oaSubscrName=_OaSubscrName_Object((1,3,6,1,4,1,629,1,50,15,6,10,1,1),_OaSubscrName_Type())
oaSubscrName.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSubscrName.setStatus(_A)
_OaSubscrDirection_Type=DirectionType
_OaSubscrDirection_Object=MibTableColumn
oaSubscrDirection=_OaSubscrDirection_Object((1,3,6,1,4,1,629,1,50,15,6,10,1,2),_OaSubscrDirection_Type())
oaSubscrDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSubscrDirection.setStatus(_A)
class _OaSubscrAccNmAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_D,1),('enable',2),('disable',3),('pause',4),('resume',5),('clear',6)))
_OaSubscrAccNmAdminStatus_Type.__name__=_C
_OaSubscrAccNmAdminStatus_Object=MibTableColumn
oaSubscrAccNmAdminStatus=_OaSubscrAccNmAdminStatus_Object((1,3,6,1,4,1,629,1,50,15,6,10,1,3),_OaSubscrAccNmAdminStatus_Type())
oaSubscrAccNmAdminStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:oaSubscrAccNmAdminStatus.setStatus(_A)
class _OaSubscrAccNmOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('active',2),('paused',3),('disabled',4)))
_OaSubscrAccNmOperStatus_Type.__name__=_C
_OaSubscrAccNmOperStatus_Object=MibTableColumn
oaSubscrAccNmOperStatus=_OaSubscrAccNmOperStatus_Object((1,3,6,1,4,1,629,1,50,15,6,10,1,4),_OaSubscrAccNmOperStatus_Type())
oaSubscrAccNmOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSubscrAccNmOperStatus.setStatus(_A)
_OaSubscrAccNmConformingBytes_Type=AccountCouter
_OaSubscrAccNmConformingBytes_Object=MibTableColumn
oaSubscrAccNmConformingBytes=_OaSubscrAccNmConformingBytes_Object((1,3,6,1,4,1,629,1,50,15,6,10,1,6),_OaSubscrAccNmConformingBytes_Type())
oaSubscrAccNmConformingBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSubscrAccNmConformingBytes.setStatus(_A)
_OaSubscrAccNmHighConformingBytes_Type=Counter32
_OaSubscrAccNmHighConformingBytes_Object=MibTableColumn
oaSubscrAccNmHighConformingBytes=_OaSubscrAccNmHighConformingBytes_Object((1,3,6,1,4,1,629,1,50,15,6,10,1,7),_OaSubscrAccNmHighConformingBytes_Type())
oaSubscrAccNmHighConformingBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSubscrAccNmHighConformingBytes.setStatus(_A)
_OaSubscrAccNmLowConformingBytes_Type=Counter32
_OaSubscrAccNmLowConformingBytes_Object=MibTableColumn
oaSubscrAccNmLowConformingBytes=_OaSubscrAccNmLowConformingBytes_Object((1,3,6,1,4,1,629,1,50,15,6,10,1,8),_OaSubscrAccNmLowConformingBytes_Type())
oaSubscrAccNmLowConformingBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSubscrAccNmLowConformingBytes.setStatus(_A)
_OaSubscrAccNmExceedingBytes_Type=AccountCouter
_OaSubscrAccNmExceedingBytes_Object=MibTableColumn
oaSubscrAccNmExceedingBytes=_OaSubscrAccNmExceedingBytes_Object((1,3,6,1,4,1,629,1,50,15,6,10,1,9),_OaSubscrAccNmExceedingBytes_Type())
oaSubscrAccNmExceedingBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSubscrAccNmExceedingBytes.setStatus(_A)
_OaSubscrAccNmHighExceedingBytes_Type=Counter32
_OaSubscrAccNmHighExceedingBytes_Object=MibTableColumn
oaSubscrAccNmHighExceedingBytes=_OaSubscrAccNmHighExceedingBytes_Object((1,3,6,1,4,1,629,1,50,15,6,10,1,10),_OaSubscrAccNmHighExceedingBytes_Type())
oaSubscrAccNmHighExceedingBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSubscrAccNmHighExceedingBytes.setStatus(_A)
_OaSubscrAccNmLowExceedingBytes_Type=Counter32
_OaSubscrAccNmLowExceedingBytes_Object=MibTableColumn
oaSubscrAccNmLowExceedingBytes=_OaSubscrAccNmLowExceedingBytes_Object((1,3,6,1,4,1,629,1,50,15,6,10,1,11),_OaSubscrAccNmLowExceedingBytes_Type())
oaSubscrAccNmLowExceedingBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSubscrAccNmLowExceedingBytes.setStatus(_A)
_OaSubscrAccNmConformingPackets_Type=AccountCouter
_OaSubscrAccNmConformingPackets_Object=MibTableColumn
oaSubscrAccNmConformingPackets=_OaSubscrAccNmConformingPackets_Object((1,3,6,1,4,1,629,1,50,15,6,10,1,12),_OaSubscrAccNmConformingPackets_Type())
oaSubscrAccNmConformingPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSubscrAccNmConformingPackets.setStatus(_A)
_OaSubscrAccNmHighConformingPackets_Type=Counter32
_OaSubscrAccNmHighConformingPackets_Object=MibTableColumn
oaSubscrAccNmHighConformingPackets=_OaSubscrAccNmHighConformingPackets_Object((1,3,6,1,4,1,629,1,50,15,6,10,1,13),_OaSubscrAccNmHighConformingPackets_Type())
oaSubscrAccNmHighConformingPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSubscrAccNmHighConformingPackets.setStatus(_A)
_OaSubscrAccNmLowConformingPackets_Type=Counter32
_OaSubscrAccNmLowConformingPackets_Object=MibTableColumn
oaSubscrAccNmLowConformingPackets=_OaSubscrAccNmLowConformingPackets_Object((1,3,6,1,4,1,629,1,50,15,6,10,1,14),_OaSubscrAccNmLowConformingPackets_Type())
oaSubscrAccNmLowConformingPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSubscrAccNmLowConformingPackets.setStatus(_A)
_OaSubscrAccNmExceedingPackets_Type=AccountCouter
_OaSubscrAccNmExceedingPackets_Object=MibTableColumn
oaSubscrAccNmExceedingPackets=_OaSubscrAccNmExceedingPackets_Object((1,3,6,1,4,1,629,1,50,15,6,10,1,15),_OaSubscrAccNmExceedingPackets_Type())
oaSubscrAccNmExceedingPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSubscrAccNmExceedingPackets.setStatus(_A)
_OaSubscrAccNmHighExceedingPackets_Type=Counter32
_OaSubscrAccNmHighExceedingPackets_Object=MibTableColumn
oaSubscrAccNmHighExceedingPackets=_OaSubscrAccNmHighExceedingPackets_Object((1,3,6,1,4,1,629,1,50,15,6,10,1,16),_OaSubscrAccNmHighExceedingPackets_Type())
oaSubscrAccNmHighExceedingPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSubscrAccNmHighExceedingPackets.setStatus(_A)
_OaSubscrAccNmLowExceedingPackets_Type=Counter32
_OaSubscrAccNmLowExceedingPackets_Object=MibTableColumn
oaSubscrAccNmLowExceedingPackets=_OaSubscrAccNmLowExceedingPackets_Object((1,3,6,1,4,1,629,1,50,15,6,10,1,17),_OaSubscrAccNmLowExceedingPackets_Type())
oaSubscrAccNmLowExceedingPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSubscrAccNmLowExceedingPackets.setStatus(_A)
_OaSubscrAccNm64ConformingBytes_Type=AccountCounter64
_OaSubscrAccNm64ConformingBytes_Object=MibTableColumn
oaSubscrAccNm64ConformingBytes=_OaSubscrAccNm64ConformingBytes_Object((1,3,6,1,4,1,629,1,50,15,6,10,1,18),_OaSubscrAccNm64ConformingBytes_Type())
oaSubscrAccNm64ConformingBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSubscrAccNm64ConformingBytes.setStatus(_A)
_OaSubscrAccNm64ExceedingBytes_Type=AccountCounter64
_OaSubscrAccNm64ExceedingBytes_Object=MibTableColumn
oaSubscrAccNm64ExceedingBytes=_OaSubscrAccNm64ExceedingBytes_Object((1,3,6,1,4,1,629,1,50,15,6,10,1,19),_OaSubscrAccNm64ExceedingBytes_Type())
oaSubscrAccNm64ExceedingBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:oaSubscrAccNm64ExceedingBytes.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'SubscriberName':SubscriberName,'DirectionType':DirectionType,'AccountCouter':AccountCouter,'AccountCounter64':AccountCounter64,'nbase':nbase,'nbSwitchG1':nbSwitchG1,'nbSwitchG1Il':nbSwitchG1Il,'oaSubscriberConfig':oaSubscriberConfig,'oaSubscrConfigGen':oaSubscrConfigGen,'oaSubscrAccounting':oaSubscrAccounting,'oaSubscrAccNameTable':oaSubscrAccNameTable,'oaSubscrAccNameEntry':oaSubscrAccNameEntry,_G:oaSubscrName,_H:oaSubscrDirection,'oaSubscrAccNmAdminStatus':oaSubscrAccNmAdminStatus,'oaSubscrAccNmOperStatus':oaSubscrAccNmOperStatus,'oaSubscrAccNmConformingBytes':oaSubscrAccNmConformingBytes,'oaSubscrAccNmHighConformingBytes':oaSubscrAccNmHighConformingBytes,'oaSubscrAccNmLowConformingBytes':oaSubscrAccNmLowConformingBytes,'oaSubscrAccNmExceedingBytes':oaSubscrAccNmExceedingBytes,'oaSubscrAccNmHighExceedingBytes':oaSubscrAccNmHighExceedingBytes,'oaSubscrAccNmLowExceedingBytes':oaSubscrAccNmLowExceedingBytes,'oaSubscrAccNmConformingPackets':oaSubscrAccNmConformingPackets,'oaSubscrAccNmHighConformingPackets':oaSubscrAccNmHighConformingPackets,'oaSubscrAccNmLowConformingPackets':oaSubscrAccNmLowConformingPackets,'oaSubscrAccNmExceedingPackets':oaSubscrAccNmExceedingPackets,'oaSubscrAccNmHighExceedingPackets':oaSubscrAccNmHighExceedingPackets,'oaSubscrAccNmLowExceedingPackets':oaSubscrAccNmLowExceedingPackets,'oaSubscrAccNm64ConformingBytes':oaSubscrAccNm64ConformingBytes,'oaSubscrAccNm64ExceedingBytes':oaSubscrAccNm64ExceedingBytes})