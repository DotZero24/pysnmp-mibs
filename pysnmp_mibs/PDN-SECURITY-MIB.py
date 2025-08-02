_N='securityMgrSubnetMask'
_M='securityMgrIpAddress'
_L='noAccess'
_K='newSecurityMgrIpAddress'
_J='devSecurityMgrIpAddress'
_I='readWrite'
_H='read-only'
_G='PDN-SECURITY-MIB'
_F='enable'
_E='disable'
_D='deprecated'
_C='Integer32'
_B='mandatory'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pdn_security,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-security')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
class _DevSecurityMgrValidation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_DevSecurityMgrValidation_Type.__name__=_C
_DevSecurityMgrValidation_Object=MibScalar
devSecurityMgrValidation=_DevSecurityMgrValidation_Object((1,3,6,1,4,1,1795,2,24,2,8,1),_DevSecurityMgrValidation_Type())
devSecurityMgrValidation.setMaxAccess(_A)
if mibBuilder.loadTexts:devSecurityMgrValidation.setStatus(_B)
_DevSecurityMgrMaxNumber_Type=Integer32
_DevSecurityMgrMaxNumber_Object=MibScalar
devSecurityMgrMaxNumber=_DevSecurityMgrMaxNumber_Object((1,3,6,1,4,1,1795,2,24,2,8,2),_DevSecurityMgrMaxNumber_Type())
devSecurityMgrMaxNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:devSecurityMgrMaxNumber.setStatus(_B)
_DevSecurityMgrCurrentNumber_Type=Integer32
_DevSecurityMgrCurrentNumber_Object=MibScalar
devSecurityMgrCurrentNumber=_DevSecurityMgrCurrentNumber_Object((1,3,6,1,4,1,1795,2,24,2,8,3),_DevSecurityMgrCurrentNumber_Type())
devSecurityMgrCurrentNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:devSecurityMgrCurrentNumber.setStatus(_B)
_DevSecurityMgrTable_Object=MibTable
devSecurityMgrTable=_DevSecurityMgrTable_Object((1,3,6,1,4,1,1795,2,24,2,8,4))
if mibBuilder.loadTexts:devSecurityMgrTable.setStatus(_D)
_DevSecurityMgrEntry_Object=MibTableRow
devSecurityMgrEntry=_DevSecurityMgrEntry_Object((1,3,6,1,4,1,1795,2,24,2,8,4,1))
devSecurityMgrEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:devSecurityMgrEntry.setStatus(_D)
_DevSecurityMgrIpAddress_Type=IpAddress
_DevSecurityMgrIpAddress_Object=MibTableColumn
devSecurityMgrIpAddress=_DevSecurityMgrIpAddress_Object((1,3,6,1,4,1,1795,2,24,2,8,4,1,1),_DevSecurityMgrIpAddress_Type())
devSecurityMgrIpAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:devSecurityMgrIpAddress.setStatus(_D)
class _DevSecurityMgrAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('read',1),(_I,2)))
_DevSecurityMgrAccess_Type.__name__=_C
_DevSecurityMgrAccess_Object=MibTableColumn
devSecurityMgrAccess=_DevSecurityMgrAccess_Object((1,3,6,1,4,1,1795,2,24,2,8,4,1,2),_DevSecurityMgrAccess_Type())
devSecurityMgrAccess.setMaxAccess(_A)
if mibBuilder.loadTexts:devSecurityMgrAccess.setStatus(_D)
_NewSecurityMgrTable_Object=MibTable
newSecurityMgrTable=_NewSecurityMgrTable_Object((1,3,6,1,4,1,1795,2,24,2,8,5))
if mibBuilder.loadTexts:newSecurityMgrTable.setStatus(_D)
_NewSecurityMgrEntry_Object=MibTableRow
newSecurityMgrEntry=_NewSecurityMgrEntry_Object((1,3,6,1,4,1,1795,2,24,2,8,5,1))
newSecurityMgrEntry.setIndexNames((0,_G,_K))
if mibBuilder.loadTexts:newSecurityMgrEntry.setStatus(_D)
_NewSecurityMgrIpAddress_Type=IpAddress
_NewSecurityMgrIpAddress_Object=MibTableColumn
newSecurityMgrIpAddress=_NewSecurityMgrIpAddress_Object((1,3,6,1,4,1,1795,2,24,2,8,5,1,1),_NewSecurityMgrIpAddress_Type())
newSecurityMgrIpAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:newSecurityMgrIpAddress.setStatus(_D)
class _NewSecurityMgrAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('read',1),(_I,2),(_L,3),('telnetNoAccess',4),('telnetRead',5),('telnetReadWrite',6)))
_NewSecurityMgrAccess_Type.__name__=_C
_NewSecurityMgrAccess_Object=MibTableColumn
newSecurityMgrAccess=_NewSecurityMgrAccess_Object((1,3,6,1,4,1,1795,2,24,2,8,5,1,2),_NewSecurityMgrAccess_Type())
newSecurityMgrAccess.setMaxAccess(_A)
if mibBuilder.loadTexts:newSecurityMgrAccess.setStatus(_D)
_NewSecurityMgrSubnetMask_Type=IpAddress
_NewSecurityMgrSubnetMask_Object=MibTableColumn
newSecurityMgrSubnetMask=_NewSecurityMgrSubnetMask_Object((1,3,6,1,4,1,1795,2,24,2,8,5,1,3),_NewSecurityMgrSubnetMask_Type())
newSecurityMgrSubnetMask.setMaxAccess(_A)
if mibBuilder.loadTexts:newSecurityMgrSubnetMask.setStatus(_D)
class _DevSecurityTelnetSourceValidation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_DevSecurityTelnetSourceValidation_Type.__name__=_C
_DevSecurityTelnetSourceValidation_Object=MibScalar
devSecurityTelnetSourceValidation=_DevSecurityTelnetSourceValidation_Object((1,3,6,1,4,1,1795,2,24,2,8,6),_DevSecurityTelnetSourceValidation_Type())
devSecurityTelnetSourceValidation.setMaxAccess(_A)
if mibBuilder.loadTexts:devSecurityTelnetSourceValidation.setStatus(_B)
class _DevSecurityFtpSourceValidation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_DevSecurityFtpSourceValidation_Type.__name__=_C
_DevSecurityFtpSourceValidation_Object=MibScalar
devSecurityFtpSourceValidation=_DevSecurityFtpSourceValidation_Object((1,3,6,1,4,1,1795,2,24,2,8,7),_DevSecurityFtpSourceValidation_Type())
devSecurityFtpSourceValidation.setMaxAccess(_A)
if mibBuilder.loadTexts:devSecurityFtpSourceValidation.setStatus(_B)
_SecurityMgrTable_Object=MibTable
securityMgrTable=_SecurityMgrTable_Object((1,3,6,1,4,1,1795,2,24,2,8,8))
if mibBuilder.loadTexts:securityMgrTable.setStatus(_B)
_SecurityMgrEntry_Object=MibTableRow
securityMgrEntry=_SecurityMgrEntry_Object((1,3,6,1,4,1,1795,2,24,2,8,8,1))
securityMgrEntry.setIndexNames((0,_G,_M),(0,_G,_N))
if mibBuilder.loadTexts:securityMgrEntry.setStatus(_B)
_SecurityMgrIpAddress_Type=IpAddress
_SecurityMgrIpAddress_Object=MibTableColumn
securityMgrIpAddress=_SecurityMgrIpAddress_Object((1,3,6,1,4,1,1795,2,24,2,8,8,1,1),_SecurityMgrIpAddress_Type())
securityMgrIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:securityMgrIpAddress.setStatus(_B)
_SecurityMgrSubnetMask_Type=IpAddress
_SecurityMgrSubnetMask_Object=MibTableColumn
securityMgrSubnetMask=_SecurityMgrSubnetMask_Object((1,3,6,1,4,1,1795,2,24,2,8,8,1,2),_SecurityMgrSubnetMask_Type())
securityMgrSubnetMask.setMaxAccess(_H)
if mibBuilder.loadTexts:securityMgrSubnetMask.setStatus(_B)
class _SecurityMgrSnmpAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('readOnly',1),(_I,2),(_L,3)))
_SecurityMgrSnmpAccess_Type.__name__=_C
_SecurityMgrSnmpAccess_Object=MibTableColumn
securityMgrSnmpAccess=_SecurityMgrSnmpAccess_Object((1,3,6,1,4,1,1795,2,24,2,8,8,1,3),_SecurityMgrSnmpAccess_Type())
securityMgrSnmpAccess.setMaxAccess(_A)
if mibBuilder.loadTexts:securityMgrSnmpAccess.setStatus(_B)
class _SecurityMgrTelnetAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SecurityMgrTelnetAccess_Type.__name__=_C
_SecurityMgrTelnetAccess_Object=MibTableColumn
securityMgrTelnetAccess=_SecurityMgrTelnetAccess_Object((1,3,6,1,4,1,1795,2,24,2,8,8,1,4),_SecurityMgrTelnetAccess_Type())
securityMgrTelnetAccess.setMaxAccess(_A)
if mibBuilder.loadTexts:securityMgrTelnetAccess.setStatus(_B)
class _SecurityMgrFtpAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SecurityMgrFtpAccess_Type.__name__=_C
_SecurityMgrFtpAccess_Object=MibTableColumn
securityMgrFtpAccess=_SecurityMgrFtpAccess_Object((1,3,6,1,4,1,1795,2,24,2,8,8,1,5),_SecurityMgrFtpAccess_Type())
securityMgrFtpAccess.setMaxAccess(_A)
if mibBuilder.loadTexts:securityMgrFtpAccess.setStatus(_B)
class _SecurityMgrTrapAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('trapAccess',1),('noTrapAccess',2)))
_SecurityMgrTrapAccess_Type.__name__=_C
_SecurityMgrTrapAccess_Object=MibTableColumn
securityMgrTrapAccess=_SecurityMgrTrapAccess_Object((1,3,6,1,4,1,1795,2,24,2,8,8,1,6),_SecurityMgrTrapAccess_Type())
securityMgrTrapAccess.setMaxAccess(_A)
if mibBuilder.loadTexts:securityMgrTrapAccess.setStatus(_D)
_SecurityMgrRowStatus_Type=RowStatus
_SecurityMgrRowStatus_Object=MibTableColumn
securityMgrRowStatus=_SecurityMgrRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,8,8,1,7),_SecurityMgrRowStatus_Type())
securityMgrRowStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:securityMgrRowStatus.setStatus(_B)
class _DevSecuritySNMPMgrAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_DevSecuritySNMPMgrAccess_Type.__name__=_C
_DevSecuritySNMPMgrAccess_Object=MibScalar
devSecuritySNMPMgrAccess=_DevSecuritySNMPMgrAccess_Object((1,3,6,1,4,1,1795,2,24,2,8,9),_DevSecuritySNMPMgrAccess_Type())
devSecuritySNMPMgrAccess.setMaxAccess(_A)
if mibBuilder.loadTexts:devSecuritySNMPMgrAccess.setStatus(_B)
mibBuilder.exportSymbols(_G,**{'devSecurityMgrValidation':devSecurityMgrValidation,'devSecurityMgrMaxNumber':devSecurityMgrMaxNumber,'devSecurityMgrCurrentNumber':devSecurityMgrCurrentNumber,'devSecurityMgrTable':devSecurityMgrTable,'devSecurityMgrEntry':devSecurityMgrEntry,_J:devSecurityMgrIpAddress,'devSecurityMgrAccess':devSecurityMgrAccess,'newSecurityMgrTable':newSecurityMgrTable,'newSecurityMgrEntry':newSecurityMgrEntry,_K:newSecurityMgrIpAddress,'newSecurityMgrAccess':newSecurityMgrAccess,'newSecurityMgrSubnetMask':newSecurityMgrSubnetMask,'devSecurityTelnetSourceValidation':devSecurityTelnetSourceValidation,'devSecurityFtpSourceValidation':devSecurityFtpSourceValidation,'securityMgrTable':securityMgrTable,'securityMgrEntry':securityMgrEntry,_M:securityMgrIpAddress,_N:securityMgrSubnetMask,'securityMgrSnmpAccess':securityMgrSnmpAccess,'securityMgrTelnetAccess':securityMgrTelnetAccess,'securityMgrFtpAccess':securityMgrFtpAccess,'securityMgrTrapAccess':securityMgrTrapAccess,'securityMgrRowStatus':securityMgrRowStatus,'devSecuritySNMPMgrAccess':devSecuritySNMPMgrAccess})